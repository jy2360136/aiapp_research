# 手机端测试术语与混合开发原理

面向产品经理的通俗解释。你有 Vue3、Python、Java 和 PC 前后端经验，下面尽量用你熟悉的类比说明。

## 1. UIAutomator 界面树是什么？

### 一句话

它是 Android 系统从当前屏幕上“读取出来的一棵页面结构树”，不是普通日志，也不是截图。

### 它和用户看到的关系

- 你能看到的按钮、文字、输入框，在 Android 内部通常对应一棵节点树。
- UIAutomator 会遍历这棵树，输出每个节点的：
  - 类型：TextView、EditText、Button、WebView 等；
  - 文本：节点上暴露的 `text`；
  - 描述：给辅助功能用的 `content-desc`；
  - 是否可点击、是否可滚动；
  - 坐标范围；
  - 层级关系。
- 自动化测试工具、部分无障碍服务、读屏软件都依赖类似的结构信息来定位和控制页面。

### 为什么它不是“日志”

- 截图是像素；
- logcat 是程序运行日志；
- UI 树是“页面上现在有哪些控件、控件说什么、能不能点”的结构化数据。

### 为什么截图里有 AI 正文，但 UI 树里没有？

说明这段正文是“画出来的”，但没有以可访问文本节点的形式暴露给 Android 的无障碍体系。常见原因包括：

- 自绘控件/Canvas 绘制；
- WebView 内部内容没有形成可访问节点；
- Compose/Flutter/RN 组件没有正确设置语义；
- 流式文本被放在一个不可访问的容器里；
- 页面使用了图片化文本。

### 这对用户意味着什么

- 对普通视力用户：可能完全看不出问题，截图和视觉都正常。
- 对 TalkBack 读屏用户：可能只能读到导航、输入框和免责声明，读不到核心回答。
- 对测试/自动化：无法通过文本定位答案，只能依赖截图 OCR，测试成本和误判率都会上升。

### 当前结论边界

UIAutomator 树缺失是已确认事实；“读屏用户一定读不到”还需要真实开启 TalkBack 复测。但由于两者都依赖 Android AccessibilityNodeInfo，风险很高，不能忽略。

## 2. PSS、RSS、Java Heap、Native Heap、Graphics、Views、Activities

| 术语 | 通俗解释 | PC 类比 |
|---|---|---|
| PSS | Android 按共享内存比例分摊后的进程内存近似值，最适合看单个 App 占用 | 类似任务管理器里“这个进程实际占了多少” |
| RSS | 进程驻留物理内存，会重复计算共享库和共享页 | 进程真实占用的物理页总量，通常比 PSS 大 |
| Java Heap | Java/Kotlin 对象占用的堆 | JVM Heap |
| Native Heap | C/C++/Native 库分配的内存 | 非 JVM 的本地内存，图片解码、音视频、图表、WebView 引擎等常会用到 |
| Graphics | 图形缓冲区，主要和绘制、动画、图片、图表相关 | GPU/显存或绘图缓冲 |
| Views | 当前进程里 Android View 控件数量 | 类似 DOM 节点数量 |
| Activities | 当前进程里存活的 Android 页面实例数量 | 类似前端路由页面实例 |
| WebViews | 当前进程里存活的 WebView 实例数量 | 类似同时开了几个嵌入式浏览器 |

### 为什么 PSS 和 RSS 都重要

- PSS 更适合判断“这个 App 对系统造成的近似负担”。
- RSS 更容易看出进程实际驻留了多少物理内存。
- 不同 Android 版本、厂商和统计口径会不同，不能只看一个数字。

### 588 MB 意味着什么

这是一个偏高的进程内存峰值，尤其对于中端手机。它不一定立刻导致崩溃，但会带来：

- 系统更容易触发 Low Memory Killer；
- 返回其他 App 后更容易被系统杀掉；
- 页面切换、图表渲染和再次打开 App 更慢；
- 低端机和多任务场景更明显。

### 为什么不能直接叫“内存泄漏”

“内存泄漏”通常指同一路径重复执行后，内存持续单调上升，且返回首页后不回落。当前掌小宝的证据是：

- 峰值高：是；
- 回落慢：是；
- 从第 3 轮到第 4 轮不再继续上涨：说明可能是高占用/释放延迟，而不是明确的持续泄漏；
- 系统出现 LowMem 杀进程：说明高占用已经产生实际影响。

所以更准确的缺陷名是“高风险峰值内存与释放滞后”，后续再用 heap dump 判断是否为泄漏。

## 3. pushservice 是什么？

在 Android 进程列表里，你可能看到：

- `dongzheng.ai.android.phone`
- `dongzheng.ai.android.phone:pushservice`

前者是主进程，后者是同一个 App 包下的推送子进程。它的作用通常是：

- 接收厂商推送/长连接消息；
- 在 App 退到后台后接收通知；
- 让营销、行情提醒、系统消息到达用户。

它不是“另一个 App”，但会额外占内存。掌小宝退出记录中曾看到：

- 主进程 RSS 约 510 MB；
- pushservice RSS 约 165 MB；
- WebView 沙箱进程 RSS 约 186 MB。

因此从最近任务划掉后，用户感觉“App 关了”，实际上可能还有推送进程或 WebView 子进程短暂存在或重启。是否立即清掉取决于系统、厂商和 App 的 Service 配置。

## 4. WebView 是什么？

WebView 是 Android 内置的浏览器控件，底层通常使用 Chromium/Blink 引擎。它可以让原生 App 打开 H5 页面。

### 和 PC 的类比

你说的：

> 通达信这种 C 客户端塞入一个 Chrome 引擎，从而往里面塞网页

这个理解方向是对的。更准确的类比是：

- 桌面端：Electron / CEF / WebView2 在原生窗口里嵌入 Chromium；
- Android：Java/Kotlin Activity 里放入一个 WebView 控件；
- WebView 加载 HTML/CSS/JS，执行浏览器渲染；
- 原生容器负责窗口、权限、下载、登录态、支付、文件、相机等能力。

### 和 iframe 的区别

- `iframe` 是网页内部的子页面容器，父子都是浏览器上下文。
- `WebView` 是原生控件里嵌入一个浏览器引擎，外面是 Java/Kotlin，里面是 Web。
- 一个页面可以同时存在多个 WebView；“4 个 WebView”意味着同时有 4 个浏览器载体或渲染上下文，不能简单当成 4 个 iframe。

## 5. “安卓原生 + 同花顺 H5 模块”是什么原理？

合理的架构通常是：

```text
Android 原生外壳（Java/Kotlin）
  ├─ 原生页面：首页、自选、交易、账户、权限、推送
  ├─ WebView 容器
  │    └─ H5 页面：资讯、研报、活动、部分行情/图表/AI 页面
  └─ JSBridge / WebMessage
       ├─ H5 调原生：打开相机、获取登录态、跳转交易、保存文件
       └─ 原生调 H5：注入用户信息、刷新页面、回传事件
```

常见通信方式：

- `addJavascriptInterface`：原生暴露 Java 对象给 JS；
- `evaluateJavascript`：原生执行 JS；
- `WebViewClient` / `WebChromeClient`：拦截跳转、处理权限和加载状态；
- URL Scheme / Deep Link：H5 通过自定义链接拉起原生页面；
- WebMessage / JSBridge：封装成统一的前端调用协议。

### 为什么 App 会这样开发

- H5 可以跨 Android/iOS 复用；
- 内容和活动可以热更新，不必每次发版；
- 原生页面性能更好、系统能力更完整；
- 混合架构能平衡“体验”和“迭代速度”。

### 代价

- WebView 内存占用高；
- 首屏可能受 H5 下载、JS 执行、接口请求影响；
- 原生与 H5 的登录态、返回键、标题栏、埋点、错误态容易不一致；
- H5 的无障碍语义容易不完整；
- 桥接调用失败时容易出现“页面空白但无提示”。

### 怎样验证是不是 H5

可以看：

- Activity 名里是否出现 `WebViewActivity`、`HybridActivity`；
- `dumpsys meminfo` 是否有多个 WebView；
- UI 树中是否出现 `android.webkit.WebView`；
- 页面加载时是否出现浏览器式白屏/JS 错误；
- 网络请求里是否加载 HTML/JS/CSS 资源。

仅凭“页面看起来像网页”不能下结论；最终要以包结构、Activity、WebView 和日志为准。

## 6. 如何判断一个问题是“用户可见 Bug”还是“测试工具问题”

### 用户可见

满足任意一条：

- 普通用户按正常步骤能看到错误/空白/卡顿；
- 页面无法完成预期任务；
- 按钮文案和行为不一致；
- 网络失败后没有重试或明确错误提示；
- 读屏用户无法获取核心内容。

### 测试工具/无障碍问题

满足：

- 视觉页面正常；
- 但 UIAutomator/自动化工具读不到正文或控件；
- 普通用户不受影响，但 TalkBack、自动化、质检系统受影响。

这类问题仍应记录，因为：

- 无障碍是产品合规和用户覆盖的一部分；
- 自动化测试会变得不可靠；
- 未来投顾留痕、答案抽检、内容审核都会受影响。

## 7. 手机杀进程后为什么“还有内存”

- 杀进程会释放该进程的私有内存；
- 系统仍会保留文件缓存、页面缓存、共享库、GPU 缓存、ZRAM 等；
- Android 的设计目标是“尽量用满空闲内存做缓存”，不是一杀进程就让总内存归零；
- 从最近任务划掉不一定等于系统真正 force-stop；在本次荣耀测试机上，主进程和推送进程确实退出了，PSS 变为 0；
- 设置里的“强行停止”最彻底，但用户不应该靠手动杀进程维持体验。

## 8. 产品经理应关注的指标

不要只看“内存数字”，建议同时记录：

- 冷启动首帧时间；
- 首内容时间；
- 主要模块可交互时间；
- 首页 PSS；
- 重路径峰值 PSS；
- 返回首页 30/60/120 秒回落；
- WebView 数量；
- Activity/View 数量；
- 系统 LowMem/ExitInfo；
- 读屏可读性；
- AI 首问成功率、P95 时延、错误率、重试成功率。


## 9. 冷启动、温启动、热启动分别是什么

这三个词描述的是“App 进程和页面还在不在内存里”，不是“有没有缓存文件”。

### 冷启动

- App 进程不存在；
- 系统需要重新创建进程；
- 重新加载 Application、Activity、资源、网络库、图片库、WebView 引擎等；
- 然后才请求接口、渲染页面。

冷启动不代表完全没有缓存。它仍然可能读取 HTTP 磁盘缓存、图片缓存、本地数据库、SharedPreferences 和上次保存的数据。但这些缓存不能省掉“重新创建进程”的成本。

### 温启动

- 进程还在；
- 原 Activity/页面已经被销毁；
- 再次进入时需要重建页面和部分数据。

可以类比为浏览器进程还在，但标签页被关掉后重新打开一个。

### 热启动

- App 进程还在；
- Activity/页面也还在；
- 用户只是从后台切回前台；
- 系统直接恢复原有界面和状态。

这是最快的场景，可能只需要几十到几百毫秒。

### 为什么冷启动慢不一定等于缓存没命中

冷启动同时包含进程创建、类加载、SO/Native 库加载、首页 Activity 初始化、Compose/View 渲染、图片字体 WebView 初始化、接口请求和图表绘制。即使接口用了缓存，WebView 和大量卡片仍可能拖慢首屏。

## 10. WebView 一般占多少内存

没有固定标准，取决于 Android/Chromium 版本、页面复杂度、图片/视频/图表、WebView 数量、是否多个渲染进程、硬件加速和缓存大小。

粗略量级，仅用于产品沟通：

| 场景 | 粗略量级 | 说明 |
|---|---:|---|
| 空白/极简 WebView | 约 30–80 MB | 仅引擎和最小页面 |
| 普通 H5 页面 | 约 60–150 MB | 图片、字体、JS 框架和接口数据 |
| 图表/长列表/多媒体 H5 | 100–300 MB 或更高 | 取决于缓存和渲染 |

这些不是硬标准，验收必须用同一设备、同一版本、同一路径的 PSS 实测。

### “4 个 WebView”是不是 4 个 Chrome 引擎

不一定完全是四个独立 Chrome 进程。`dumpsys meminfo` 里的 `WebViews` 更像“当前进程里存活的 WebView 对象数量”。不同 WebView 可能共享部分 Chromium 库、GPU 资源和渲染进程，但也可能各自带来独立页面缓存和 JS 上下文。

因此 4 个 WebView 一定意味着“至少 4 个页面容器/上下文需要治理”，但不能简单算成 `4 × 150 MB`，也不能当成免费的 iframe。

## 11. 首页多个功能卡片，是不是每个卡片都要一个 WebView

不一定，常见有四种做法：

### A. 全部原生

卡片由 Android 原生控件绘制，性能和无障碍通常更好，但跨端复用和热更新较弱。

### B. 一个 WebView 承载整块 H5 区域

一个 WebView 里放多个 HTML 卡片或 Vue/React 组件，卡片之间共享 JS 上下文，内存相对可控。

### C. 一个 WebView 内用 iframe 嵌多个供应商页面

外层是一个 WebView，内部多个 iframe，类似浏览器里嵌套多个网页；iframe 可隔离，但也可能带来跨域、通信和性能问题。

### D. 每个功能卡片一个独立 WebView

每个卡片有独立浏览器上下文，隔离性强，适合不同供应商、登录态和发布节奏，但内存和启动成本最高。旧 WebView 未销毁时很容易堆到多个实例。

所以“同花顺 H5 卡片 + 东方财富 H5 卡片 + 原生对话输入框”并不意味着必然有三个 Chrome 引擎。可能是：

- 一个 WebView 中的两个 iframe/HTML 区块；
- 一个 WebView 加载聚合页；
- 两个独立 WebView；
- 原生卡片 + 单个 WebView 混合。

要判断实际实现，需要看 UI 树里出现几个 `android.webkit.WebView`、`dumpsys meminfo` 中 `WebViews` 数量、当前 Activity 是否包含多个 WebView 容器、页面切换后旧 Activity/WebView 是否销毁，以及是否存在 `WebViewPool`、`HybridActivity`、`WebViewActivity` 等结构。

掌小宝本次出现 4 个 WebView，说明至少存在 4 个存活容器；但仅凭这个计数，不能断言每个卡片都有自己的 Chrome 内核。

## 12. 原生调用 H5：是不是像传 props

方向是对的，但不完全一样。

在 Vue3 里，父组件通过 props 把数据传给子组件，因为父子组件在同一个 JS 运行时里。

原生和 H5 不在同一个运行时：

```text
Java/Kotlin 原生
  ↕ JSBridge / WebMessage / URL Scheme
JavaScript H5
```

所以原生到 H5 更像“初始状态注入 + 事件总线 + RPC 调用 + JSON 消息”，而不是 React/Vue 的活对象 props。

### 常见实现 1：注入初始状态

```javascript
window.__APP_CONFIG__ = {
  userId: "***",
  theme: "light",
  market: "A股",
  authToken: "***"
};
```

H5 启动后读取 `window.__APP_CONFIG__`，类似服务端渲染时注入的 `initialState`。

### 常见实现 2：postMessage 事件

```javascript
window.postMessage({
  type: "MARKET_DATA_UPDATED",
  payload: { code: "600519", price: 1457.7 }
}, "*");
```

```javascript
window.addEventListener("message", (event) => {
  if (event.data?.type === "MARKET_DATA_UPDATED") {
    store.updateMarket(event.data.payload);
  }
});
```

这更像事件总线，而不是 props。

### 常见实现 3：注册 JS Bridge

```java
webView.addJavascriptInterface(nativeBridge, "NativeBridge");
```

```javascript
NativeBridge.openStock("600519");
NativeBridge.getUserInfo();
```

这更像 H5 调用原生提供的一组 RPC 方法。

### 常见实现 4：URL Scheme / Deep Link

H5 触发 `app://stock?code=600519`，原生拦截 URL 并打开对应页面。

### 实际项目通常采用“握手 + 事件 + 主动拉取”

1. H5 加载完成后发送 `ready`。
2. 原生收到 `ready`，再注入用户信息或主题配置。
3. H5 把数据放进 Pinia/Redux 状态。
4. 原生后续通过 `postMessage` 推送行情、登录态或页面事件。
5. H5 通过 Bridge 调原生能力。
6. 双方带协议版本号，避免 App 与 H5 发布不同步。

### 关键坑

- H5 还没注册监听，原生就发送消息，导致消息丢失；
- 桥接只能传字符串，复杂对象需要 JSON 序列化；
- 不同供应商 H5 的字段协议容易漂移；
- 登录态/token 通过桥接传递，安全边界要严格；
- 页面刷新后状态丢失，需要重新注入或从本地缓存恢复；
- H5 没有无障碍语义，原生容器不会自动补上。

可以把 Bridge 理解为：原生和 H5 之间的一套异步 RPC + 事件总线 + 初始状态注入机制，不完全等同于 Vue3 的 props。

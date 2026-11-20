# 掌小宝 AI 调研交接文档

> 这份文档可以直接发给下一个会话/下一位同事，作为继续调研的起点。

## 0. 当前目标

继续对东莞证券「掌小宝」及五款重点 AI 证券 App 做版本化、可复现、可交接的产品与体验测试，最终形成缺陷单、竞品矩阵、功能路线图、新版本回归结果和可追踪证据。

## 1. 工作目录与仓库

- 本机工作目录：`D:\aiapp竞品调研`
- GitHub：https://github.com/jy2360136/aiapp_research
- 当前默认分支：`main`
- 仓库状态：Private，已确认用于公司/家庭电脑内部同步。
- 原始敏感证据按产品和版本保存在 `research/**/raw/`，并随私有仓库同步；顶层 `.private/` 已删除。

## 2. 设备与被测 App

- 设备：HONOR `MEP-AN00`
- Android：16 / API 36
- 分辨率：1264 × 2736
- 掌小宝包名：`dongzheng.ai.android.phone`
- 当前测试版本：`1.0.0`（versionCode 100，可调试包）
- 重点竞品版本：问财 5.3.1、妙想 1.6.0、灵犀 9.30.45、涨乐财富通 2.0.6、长小牛 1.1.6。

## 3. 先看哪些文档

1. `docs/README.md`
2. `docs/executive-summary.md`
3. `docs/bug-reports-v1.0.0_20261118.md`
4. `docs/memory-and-performance.md`
5. `docs/competitor-benchmark.md`
6. `docs/product-roadmap.md`
7. `docs/technical-concepts.md`
8. `docs/competitor-login-sop.md`

## 4. 不要先看哪些目录

- `research/target-dongzheng-ai/archive/`
- `research/competitors/archive/`
- `research/**/raw/`

以上目录只用于历史追溯或原始证据核验。旧版本截图和结论不能直接当作当前版本结论。

## 5. 当前测试状态

### 掌小宝

已完成首页/盯盘、AI 对话、自选、个股详情、设置与协议页首轮采集。自选空态语义问题已撤回。AI 冷启动 5 次首问 5/5 成功；AI 正文无障碍树缺失 5/5 复现；首屏主要行情约 3.7 秒出现；重路径 PSS 峰值约 588 MB、4 个 WebView、976 个 View。

未完成：TalkBack 人工读屏、10 轮重复路径和 heap dump、正式包复测、交易只读页、低端机/弱网/长期后台。

### 东方财富妙想

已完成隐私授权、测试手机号验证码登录、登录后 AI 首页和一次“综合诊股”。未完成 Work 模式、历史/个性化/引用、长对话、无障碍和错误态。

### 其他竞品

问财、灵犀、Yomi、长小牛均已完成 AI 入口和至少一轮问答；详细结论见竞品目录 README。

## 6. 下一轮优先任务

### P0：掌小宝新版本回归

1. 记录新版本号。
2. 建立 `research/target-dongzheng-ai/screenshots/v<新版本>_<日期>/`。
3. 复测 AI 冷启动首问 20 次成功率。
4. 复测 AI 正文是否进入 UIAutomator 树。
5. 复测冷启动首内容时间、10 轮内存曲线和 WebView 数量。
6. 新版本修复后，旧截图只作对比，不能混进新版本目录。

### P1：补无障碍真实场景

开启 TalkBack，测试首问、流式生成、完成态、长回答滚动、来源打开、错误态、复制/点赞/重试/收藏。记录是否可朗读、朗读顺序、是否重复、是否能停止播报。

### P1：补竞品深测

- 妙想：Work 模式、长对话、引用、历史、个性化。
- 问财：投资记忆、自动化任务、历史/收藏、回测。
- 灵犀：多轮上下文、历史、语音、引用点击。
- Yomi：Agent 帮我选、任务 Tab、持仓上下文、风险提示。
- 长小牛：AI 正文读屏、复杂任务、历史记录。

### P2：产品规划更新

用真实测试结果更新 `docs/product-roadmap.md`。已修复问题移到“已关闭/已验证”，新增功能写清用户价值、数据依赖、合规边界和验收指标。

## 7. 截图和目录规范

```text
research/target-dongzheng-ai/
  screenshots/v1.0.0_20261118/
    README.md
    raw/
    01-盯盘/  02-对话/  03-自选/  04-交易/  05-设置与协议/
  ui-hierarchy/v1.0.0_20261118/
    raw/
  logs/v1.0.0_20261118/
    raw/
    app-internal/
  metadata/v1.0.0_20261118/
    raw/

research/competitors/
  <product>/v<version>_<date>/
    README.md
    screenshots/01-AI入口/
    screenshots/02-AI问答/
    screenshots/raw/
    ui-hierarchy/raw/
    metadata/raw/
```

命名规则：`stepNN_操作_结果.png`。每个版本 README 必须写版本号/包名/日期、测试范围、当前结论、剩余问题、下一轮优先看哪些文件。

## 8. 手机号验证码登录 SOP

1. 保持 `+86`，不要切国家。
2. 点击 `+86` 右侧的手机号输入框，不是左侧区号。
3. 输入用户授权的测试手机号。
4. 勾选/同意服务协议、隐私政策和未成年人隐私政策。
5. 点击获取验证码。
6. 立刻读取最新短信，**不要先做其他检查或写日志**。
7. 提取 6 位动态码后立即填入并点击登录。
8. 验证码约 1 分钟过期；失败就重新获取新码。
9. 公开截图必须遮盖手机号、验证码、账号名和资产信息。

完整流程见 `docs/competitor-login-sop.md`。授权手机号保存在 `docs/competitor-auth.md`，随 Private 仓库同步。

## 9. 安全边界

不执行买入、卖出、撤单、银证转账、支付、开户、风险测评提交、修改密码、退出登录、删除数据或任何资金/账户状态变化。可以执行公开行情浏览、AI 问答、只读页面，以及用户明确授权的隐私/协议同意和测试手机号登录。

## 10. 关键判断原则

- 截图可见但界面树缺失：记为“无障碍/自动化风险”，不要直接说“普通用户可见”。
- 一次内存峰值：不能直接判定泄漏。
- 同一路径重复上升且不回落：才更接近泄漏。
- 一次 AI 失败：不足以判断全量故障，要记录频次和请求上下文。
- 旧版本修复后，不要继续引用旧版本截图作为当前事实。

## 11. 下一轮开场提示词

```text
请先阅读 docs/handoff.md、docs/README.md、docs/executive-summary.md 和 docs/bug-reports-v1.0.0_20261118.md。
先确认当前掌小宝和竞品的最新版本号，再按 research/ 下的版本化目录继续。
不要读取 archive/ 和 `raw/` 作为第一入口；旧截图只用于回归对比。
先做掌小宝新版本回归，再做 TalkBack 和 10 轮内存复测，最后补妙想 Work 模式与其余竞品深测。
截图必须按功能分区和 stepNN 顺序命名，并写版本 README。
```

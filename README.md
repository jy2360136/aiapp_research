# 手机端 AI 证券 App 竞品调研与缺陷排查

本项目用于在自有测试手机上，通过 ADB 对东莞证券「掌小宝」及重点 AI 证券 App 进行可复现的界面遍历、截图、界面结构记录、异常日志采集、性能采样与产品分析。

## 当前结论入口

- [执行摘要](docs/executive-summary.md)
- [重点缺陷复现单](research/target-dongzheng-ai/05-findings/bug-reports.md)
- [内存与首屏性能说明](docs/memory-and-performance.md)
- [五款重点竞品对标](docs/competitor-benchmark.md)
- [AI 功能规划与优先级清单](docs/product-roadmap.md)
- [掌小宝页面地图](research/target-dongzheng-ai/04-navigation/page-map.md)
- [自动化脚本说明](automation/README.md)

## 产品与测试范围

- 重点产品：东莞证券「掌小宝」，包名 `dongzheng.ai.android.phone`，版本 `1.0.0`。
- 核心对象：同花顺问财、东方财富妙想、国泰海通灵犀、涨乐财富通、长小牛。
- 暂不遍历：掌证宝及其他传统综合证券 App 的完整功能。
- 设备：HONOR `MEP-AN00`，Android 16 / API 36，1264 × 2736。
- 方法：页面地图 + 截图 + UI 结构 + 当前 Activity + 点击/返回路径 + 异常日志 + 内存采样。
- 安全边界：跳过买入、卖出、撤单、转账、支付、开户、风险测评提交、修改密码、退出登录、删除等资金或账户状态操作。

## 重点发现

1. AI 首次查询历史曾返回“服务开小差了，请稍后再试”；冷启动后重试可正常返回行情、K 线、文字结论和来源。2026-11-18 追加 5 次冷启动首问均成功，判断为低频间歇问题。
2. AI 回复正文未进入 UIAutomator/自动化界面树；截图有正文，但 XML 只有导航、输入框和免责声明。TalkBack 影响尚需人工确认。
3. 冷启动 `am start -W` 约 2.1 秒，但主要行情约 3.7 秒后才出现，视觉稳定约 4.5 秒。
4. 重路径遍历出现 PSS 约 588 MB、RSS 约 743 MB、4 个 WebView、976 个 View 的峰值；后续回落到约 331 MB，暂不判定为持续泄漏。
5. 从最近任务划掉 App 后，本机记录显示主进程、pushservice 和 WebView 沙箱进程均退出；再次打开为新 PID，属于冷启动。
6. “自选空态点击语义不一致”已撤回；复测证实「添加股票」进入搜索页正常。

## 目录约定

```text
automation/                         可复现的 ADB 采集与性能脚本
docs/                               方法、性能说明、竞品对标、产品路线图
research/
  target-dongzheng-ai/
    00-metadata/                    设备与应用元数据
    01-screenshots/                 可提交的截图（敏感信息必须脱敏）
    02-ui-hierarchy/                UI XML 或脱敏结构摘要
    03-logs/                        脱敏后的日志、AI 试验与内存采样
    04-navigation/                  页面地图与复现路径
    05-findings/                    缺陷单与产品分析
  competitors/                      脱敏竞品截图与对标资料
```

## 隐私与安全

- 原始截图、原始 UI XML、原始 logcat 若可能包含账号、持仓、金额、身份信息，只保存在本机 `.private/`，不会提交 Git。
- 提交到 Git 的竞品截图已去除手机状态栏，避免暴露无关通知和个人信息。
- 自动遍历不点击交易、转账、删除、退出登录、支付及其他会改变资金/账户状态的动作。
- 仓库只保留异常摘要、复现步骤和必要且已脱敏的堆栈片段。

## 运行前置

1. 手机开启开发者选项与 USB 调试，并授权本机。
2. 安装 Android SDK Platform-Tools；脚本会自动查找 `PATH`、WinGet 和默认 SDK 路径，也可以设置环境变量 `ADB`。
3. 连接手机后运行：

```powershell
python automation/check_connection.py
python automation/capture_page.py --label example --scope public
```

详细方法见 `automation/README.md` 和 `docs/research-method.md`。

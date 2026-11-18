# 掌小宝页面地图（进行中）

| ID | 页面 | 入口/路径 | Activity/Window | 证据 | 状态 |
|---|---|---|---|---|---|
| 001 | 盯盘首页 | 启动 App | `dongzheng.ai.android.phone/.MainActivity` | `01-screenshots/20261117_001_home.png` | 已采集 |
| 002 | AI 对话 | 顶部「对话」 | `dongzheng.ai.android.phone/.MainActivity` | `20261117_002_dialog.*` | 已采集 |
| 003 | 自选 | 顶部「自选」 | `dongzheng.ai.android.phone/.MainActivity` | `20261117_003_watchlist.*` | 已采集 |
| 004 | 侧边账户/交易栏 | 左上角菜单 | `dongzheng.ai.android.phone/.MainActivity` | `20261117_004_side_menu_redacted.*` | 已采集，已脱敏 |
| 005 | 设置首页 | 侧边栏右上角设置 | `com.zxb.home.view.HomeActivity` | 待生成脱敏证据包 | 已访问 |

## 待验证入口

- 顶部搜索
- 热门行业/概念详情
- 热门榜单详情
- 对话内推荐问题、快捷功能、语音输入
- 自选添加、搜索添加、分组/排序
- 设置：账号设置、隐私设置、显示模式、交易设置
- AI 底栏附件、语音、交易入口（交易仅观察，不执行）

## 已发现观察

- 首页、对话、自选共用固定底部 AI 输入栏与「交易」入口，主路径统一。
- AI 对话的主体回复由非标准控件/自绘区域呈现，UIAutomator 仅能取得少量输入控件；后续需要截图 + OCR/视觉分析补足。
- 侧边栏同时承载账户交易快捷入口和资产持仓；属于高敏感页面，必须脱敏。

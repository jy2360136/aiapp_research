# 掌小宝项目跨电脑交接（2026-11-20）

> 这份文档可以直接发给下一个会话或下一位同事，作为新电脑继续工作的起点。

## 1. 新电脑如何拉取所有项目资料

GitHub 仓库是 Private，新电脑必须先登录有权限的 GitHub 账号：

`https://github.com/jy2360136/aiapp_research.git`

### 1.1 新电脑还没有项目

```powershell
git clone https://github.com/jy2360136/aiapp_research.git
cd aiapp_research
git checkout main
git pull --ff-only origin main
```

### 1.2 新电脑已经有项目目录

```powershell
cd <项目目录>
git fetch origin --prune
git checkout main
git pull --ff-only origin main
```

### 1.3 拉取后检查

```powershell
git status --short --branch
git log -1 --oneline
Test-Path .private
```

预期结果：

- 当前分支为 `main`，工作区没有未提交改动。
- `.private` 返回 `False`。
- 原始证据在 `research/**/raw/`。
- 当前没有使用 Git LFS；截图、XML 和日志直接随 Git 仓库同步。
- 首次克隆可能较慢，仓库包含约 140 MB 证据资料。

如果 `git pull` 提示分支分叉，不要直接强推或重置，先执行 `git log --oneline --graph --decorate --all` 检查后再处理。

## 2. 当前工作状态

### 2.1 `.private` 已删除

- 顶层 `.private/` 已从工作区和 Git 索引彻底删除。
- `.gitignore` 已加入 `.private/`，防止再次误创建。
- 迁移了 198 个原始证据文件，约 58.36 MB。
- 完整逐文件迁移记录：`research/evidence-migration-20261120.md`。

### 2.2 原始证据的新位置

掌小宝：

```text
research/target-dongzheng-ai/
  screenshots/v1.0.0_20261118/raw/
  ui-hierarchy/v1.0.0_20261118/raw/
  logs/v1.0.0_20261118/raw/
  logs/v1.0.0_20261118/app-internal/
```

竞品：

```text
research/competitors/<产品>/<版本>/
  screenshots/raw/
  ui-hierarchy/raw/
  metadata/raw/
```

所有 JSON 中 `screenshot`、`ui_xml`、`summary` 引用都已修复，当前缺失引用为 0。原始证据中有 5 个截断/异常文件，保持原样并记录在迁移清单中。

### 2.3 原型图

主原型：

`prototypes/entry_changes/main_top_navigation.html`

底部 Dock 探索方案：

`prototypes/entry_changes/bottom_dock_variant.html`

本轮已按掌小宝真机截图统一：

- 顶部渐变与选中导航笔刷
- 首页行情卡、板块异动卡
- 自选页、对话页、设置页、隐私页、搜索页
- 对话设置按钮和底部 AI 输入区
- 交易一级入口和右上角 AI 图标属于本次需求调整，不是原 App 现状

底部方案预览已更新：

`prototypes/entry_changes/previews/bottom_dock_variant_preview.png`

### 2.4 MasterGo 设计稿

链接：

`https://mastergo.com/goto/XLF3vfGV?page_id=7255:15502&file=155018560119729`

- 已验证可以打开《AI-APP》画布。
- 当前可只读查看设计内容。
- 评论、标注和协作需要 MasterGo 登录。
- 画布中可见“对话-切图”“全局搜索”“对话”“自选”等区域。

## 3. 下一个会话第一次打开时应看什么

1. `docs/next-session-handoff-20261120.md`（本文件）
2. `docs/handoff.md`
3. `docs/README.md`
4. `docs/executive-summary.md`
5. `research/evidence-migration-20261120.md`
6. `prototypes/entry_changes/README.md`

## 4. 直接发给下一个会话的开场提示词

```text
请先读取 docs/next-session-handoff-20261120.md、docs/handoff.md、docs/README.md 和 research/evidence-migration-20261120.md。

项目仓库：https://github.com/jy2360136/aiapp_research.git
分支：main

如果当前电脑还没有项目：
git clone https://github.com/jy2360136/aiapp_research.git
cd aiapp_research
git checkout main
git pull --ff-only origin main

如果已有项目：
git fetch origin --prune
git checkout main
git pull --ff-only origin main

拉取后先运行：
git status --short --branch
Test-Path .private

预期：工作区干净，.private 不存在；原始证据在 research/**/raw/。

当前已完成：
1. .private 已彻底删除，198 个证据文件已迁移到 research 对应产品/版本目录。
2. 原型 HTML 已按掌小宝真机截图调整。
3. MasterGo《AI-APP》画布可只读访问：
https://mastergo.com/goto/XLF3vfGV?page_id=7255:15502&file=155018560119729

下一步请先确认当前 App/竞品版本，再继续 docs/handoff.md 中的测试任务。不要读取 archive/ 或 raw/ 作为第一入口；它们只用于追溯。
```

## 5. 采集脚本的新输出规则

脚本会根据安装包 `versionName` 和采集日期自动建立版本目录：

- `capture_page.py`：截图、UI XML、元数据分别进入 `screenshots`、`ui-hierarchy`、`metadata` 的版本目录。
- `capture_competitor.py`：按竞品 slug、版本和日期归档。
- `capture_exceptions.py`：原始日志进入 `logs/<版本>/raw/`。
- `ai_query_trials.py`：截图、UI、元数据分别进入对应 raw 目录。
- `startup_capture.py`：启动截图进入 `screenshots/<版本>/startup/raw/`。
- `memory_sample.py`、`memory_cycle_test.py`：采样进入 `logs/<版本>/memory/raw/`。

## 6. 安全边界

- `research/**/raw/` 可能包含账号、持仓、手机号、验证码或登录态，只允许在 Private 仓库内同步。
- 不对外分享 raw 目录。
- 不执行买入、卖出、撤单、银证转账、支付、开户、风险测评提交、修改密码、退出登录或删除账户数据。
- 需要对外展示时使用已脱敏截图、摘要或单独裁剪后的材料。

## 7. 已知事项

- 本轮修复了本地 `.git/refs/heads/main` 被全零字节污染的问题；当前本地 `main` 已重新指向远程真实历史，没有用强推覆盖远程。
- 原始证据中的 5 个损坏/异常文件已在迁移记录中标注，不要把它们当作完整截图或有效 XML 使用。

# 调研文档索引

## 第一次打开先看

1. `handoff.md`：交接给下一会话的完整上下文、任务顺序和边界。
2. `executive-summary.md`：一页结论。
3. `bug-reports-v1.0.0_20261118.md`：当前版本重点缺陷的复现顺序。
4. `competitor-benchmark.md`：五款重点竞品横向对标。
5. `product-roadmap.md`：MVP/短期/中期/长期和优先级。
6. `memory-and-performance.md`：首屏、PSS、WebView、杀进程解释。
7. `technical-concepts.md`：手机端术语与原生/H5 混合开发原理。
8. `competitor-login-sop.md`：竞品手机号验证码登录 SOP。

## 文档边界

- 本目录保存“当前有效结论”和“交接上下文”。
- 原始截图、UI 树和日志在 `research/` 下按版本归档。
- `research/*/archive/` 是旧版本平铺目录，不作为下一轮的第一入口。
- 原始敏感证据按产品和版本保存在 `research/**/raw/`，随 Private 仓库同步；它不是当前结论的第一入口，但仍是可追溯原始证据。
- 原顶层 `.private/` 已于 2026-11-20 迁移并删除，记录见 `research/evidence-migration-20261120.md`。
- `competitor-auth.md` 是测试授权信息，保存在 `docs/` 并随 Private 仓库同步。

## 版本规则

- 当前掌小宝版本：`1.0.0`，对应日期 `20261118`。
- 新版本必须新建 `v<version>_<date>` 目录，不能覆盖旧版本。
- 旧版本已修复的问题只用于回归对比，不作为当前事实。

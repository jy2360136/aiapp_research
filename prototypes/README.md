# 原型图目录

原型按“功能项目”组织，每个项目内部再区分 HTML、图片、脚本和预览图。

```text
prototypes/
  entry_changes/         入口与功能分区调整原型
```

## 当前项目

- `entry_changes/`：导航层级、交易入口、对话入口、底部 Dock 与设置页调整。

## 规则

- 每个功能项目一个目录，不把 HTML 和图片直接放在仓库根目录。
- 项目内部至少包含：
  - 根目录 HTML
  - `images/`
  - `scripts/`
  - `previews/`
  - 项目 README
- 图片资源与验证截图分开存放，便于后续复用和清理。

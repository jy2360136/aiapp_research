# entry_changes：入口与功能分区调整

## 项目目的

验证掌小宝一级功能入口、交易入口、AI 对话入口、全局输入框、底部 Dock 和设置页的调整方案。

## 目录结构

```text
entry_changes/
  README.md
  main_top_navigation.html      推荐落地：顶部业务导航 + 全局 AI 输入
  bottom_dock_variant.html      独立探索：一级导航与 AI 输入下沉到底部 Dock
  images/                       形象、背景等源图片
  scripts/                      CDP 验证与历史检查脚本
  previews/                     页面预览、交互截图和验证截图
```

## 当前方案

### 主原型

`main_top_navigation.html`

- 介绍页
- 顶部业务导航方案
- 交易提升为一级入口
- AI 对话使用右上角图标
- 各业务页底部长驻 AI 输入
- 汉堡菜单直达设置
- 设置页包含左上角返回键和居中“设置”标题

### 独立底部 Dock 方案

`bottom_dock_variant.html`

- 一级导航下沉到底部
- 底部同时承载“盯盘 / 自选 / 交易”和 AI 输入
- 对话入口固定在输入框右侧
- 推荐问句随当前页面变化

## 预览与验证

- `previews/main_top_navigation_preview.png`
- `previews/bottom_dock_variant_preview.png`
- `previews/verify-main-settings-cdp.png`
- `scripts/verify-split.js`

验证脚本会检查：

- 主原型只有两页
- 介绍页不含 Dock 迁移卡片
- 主原型不含底部 Dock 第三页
- 独立页只包含一个底部 Dock 方案
- 设置的返回键可见、标题居中
- 交易 Tab 和推荐问句联动正常
- 页面无 JavaScript 异常

## 运行方式

在仓库根目录启动支持 CDP 的 Chrome 后执行：

```powershell
node prototypes\entry_changes\scripts\verify-split.js
```

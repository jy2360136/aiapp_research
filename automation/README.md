# 自动化脚本

## 检查连接

```powershell
python automation/check_connection.py
```

## 采集当前页

公开页面：

```powershell
python automation/capture_page.py --label home
```

敏感页面（原始文件自动进入 `.private/`，公开目录只保留脱敏 XML 与摘要）：

```powershell
python automation/capture_page.py --label account_panel --scope sensitive
```

点击后并采集：

```powershell
python automation/capture_page.py --label settings --tap-x 990 --tap-y 215
```

脚本会自动把掌小宝拉到前台，并记录前台 Window、页面签名、截图、UI XML 和可交互元素摘要。检测到敏感词时，即使误传 `--scope public` 也会强制降级为敏感模式。

## 异常日志

```powershell
python automation/capture_exceptions.py --label after_click
```

原始日志写入 `.private/`；仓库仅生成经关键词筛选和基础脱敏的异常摘要。复现点击问题时，应先清空日志，再在手机/ADB 执行单个动作，最后采集。

```powershell
python automation/capture_exceptions.py --label before --clear
# 执行一次点击
python automation/capture_exceptions.py --label after
```

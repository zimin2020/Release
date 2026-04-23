# release

Windows 桌面截图贴图工具（Python）。

## 当前能力（MVP）

- `Ctrl+1`：全屏框选截图
- `Ctrl+Q`：关闭全部截图贴图
- 截图贴图支持：
  - 双击：正常图 / 缩略图切换
  - 滚轮：缩放
  - 拖拽：任意移动
  - 置顶显示
- 托盘菜单：
  - 截图
  - 关闭截图
  - 打开菜单
  - 设置（中英切换）
  - 更新日志
  - 退出

## 安装依赖

```bash
pip install -r requirements.txt
```

## 运行

```bash
python main.py
```

## 打包（建议）

```bash
python -m nuitka main.py --onefile --standalone --windows-console-mode=disable --enable-plugin=tk-inter --assume-yes-for-downloads --output-filename=release.exe
```

> 说明：10MB 以内目标很激进，建议后续配合 UPX 与依赖裁剪进一步压缩。


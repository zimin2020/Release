import ctypes

from src.release_app.app import ReleaseApp


def _enable_dpi_awareness() -> None:
    # Per-monitor DPI aware，避免高分屏下坐标与像素不一致。
    try:
        ctypes.windll.user32.SetProcessDpiAwarenessContext(ctypes.c_void_p(-4))
        return
    except (AttributeError, OSError):
        pass
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
        return
    except (AttributeError, OSError):
        pass
    try:
        ctypes.windll.user32.SetProcessDPIAware()
    except (AttributeError, OSError):
        pass


def main() -> None:
    _enable_dpi_awareness()
    app = ReleaseApp()
    app.run()


if __name__ == "__main__":
    main()

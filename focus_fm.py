import time
import pygetwindow as gw


def focus_fm():
    windows = [w for w in gw.getWindowsWithTitle("Football Manager 2023")]
    if not windows:
        return False, "Did not found the FM23 window despite knowing the process is running."

    fm_window = windows[0]
    try:
        fm_window.activate()
        time.sleep(0.2)
        return True, f"Window '{fm_window.title}' focused successfully."
    except Exception as e:
        return False, f"Couldn't focus the window error: {e}"

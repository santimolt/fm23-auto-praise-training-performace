import time
import json
import pyautogui
import pygetwindow as gw


def focus_fm():
    """
    Bring FM23 window to the foreground using pygetwindow + pyautogui.
    Works on Windows, macOS, and Linux.
    """
    # Buscar ventanas que contengan "FM" o "Football Manager"
    windows = [w for w in gw.getWindowsWithTitle("Football Manager 2023") if w.title]

    if windows:
        fm_window = windows[0]
        try:
            fm_window.activate()
            time.sleep(0.5)
            navigate_to_individual_training()
            print(f"Focused FM23 window: {fm_window.title}")
        except Exception as e:
            print(f"Could not focus FM23 window: {e}")
    else:
        print("FM23 window not found")


def navigate_to_individual_training():
    with open("config.json") as config_file:
        config = json.load(config_file)

    hotkey_str = config.get("training_section_hotkey", "ctrl+u")
    hotkey_array = [k.lower() for k in hotkey_str.split("+")]
    pyautogui.hotkey(*hotkey_array, interval=0.1)

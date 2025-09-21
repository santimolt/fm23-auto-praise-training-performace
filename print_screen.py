import time
import pyautogui
from utils import get_config


def print_screen():
    config = get_config()
    hotkey_str = config.get("print_screen_hotkey", "ctrl+p")
    hotkey_array = [k.lower() for k in hotkey_str.split("+")]

    print(f"⌨️ Printing individual training FM screen with: {hotkey_str}")

    pyautogui.hotkey(*hotkey_array)

    time.sleep(0.2)

    # Script to print to HTML:
    pyautogui.press("tab")
    time.sleep(0.1)
    pyautogui.press("tab")
    time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(0.1)

    # Script to save the Untitled in default path.
    pyautogui.press("enter")
    time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(0.1)

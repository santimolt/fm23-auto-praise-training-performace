import pyautogui
from utils import get_config
import time

def navigate_to_individual_training():
    """
    Preventively navigates to inbox to reset the individual training view (sometimes does not detect the scroll needed to show players)
    Sends the hotkey to navigate to the Individual Training section.
    Uses the hotkey defined in config.json.
    """
    config = get_config()

    inbox_hotkey_str = config.get("other_section_hotkey", "f4")
    inbox_hotkey_arr = [k.lower() for k in inbox_hotkey_str.split("+")]

    pyautogui.hotkey(*inbox_hotkey_arr)
    time.sleep(0.5)

    training_hotkey_str = config.get("training_section_hotkey", "ctrl+u")
    
    # Convert 'ctrl+u' → ['ctrl', 'u']
    training_hotkey_arr = [k.lower() for k in training_hotkey_str.split("+")]
    
    print(f"⌨️ Navigating to Individual Training using hotkey: {training_hotkey_str}")
    
    # Send the hotkey
    pyautogui.hotkey(*training_hotkey_arr)
    
    # Optional: small delay to ensure FM registers the hotkey
    time.sleep(0.2)
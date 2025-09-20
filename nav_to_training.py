import json
import pyautogui
from utils import get_config
import time

def navigate_to_individual_training():
    """
    Sends the hotkey to navigate to the Individual Training section.
    Uses the hotkey defined in config.json.
    """
    config = get_config()
    hotkey_str = config.get("training_section_hotkey", "ctrl+u")
    
    # Convert 'ctrl+u' → ['ctrl', 'u']
    hotkey_array = [k.lower() for k in hotkey_str.split("+")]
    
    print(f"⌨️ Navigating to Individual Training using hotkey: {hotkey_str}")
    
    # Send the hotkey
    pyautogui.hotkey(*hotkey_array)
    
    # Optional: small delay to ensure FM registers the hotkey
    time.sleep(0.2)
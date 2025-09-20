import json

def get_config(config_file="config.json"):
    """
    Load configuration from JSON file.
    Returns a dictionary with keys:
    - training_section_hotkey
    - min_score_to_praise
    - delay_after_hotkey
    """
    try:
        with open(config_file) as f:
            config = json.load(f)
    except FileNotFoundError:
        print(f"⚠️ Config file '{config_file}' not found. Using default values.")
        config = {}

    # Defaults
    defaults = {
        "training_section_hotkey": "ctrl+u",
        "min_score_to_praise": 7.5,
        "delay_after_hotkey": 3
    }

    # Merge user config with defaults
    for key, value in defaults.items():
        config.setdefault(key, value)

    return config
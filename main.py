import time
from utils import get_config
from focus_fm import focus_fm
from is_fm_running import is_fm_running
from nav_to_training import navigate_to_individual_training


def main():
    print("FM23 Auto Praise Players Training started.\n")

    # 1️⃣ Check if FM is running
    if not is_fm_running():
        print("❌ FM23 is not running, please start the game and retry.")
    else:
        print("✅ FM23 is running")

        # 2️⃣ Bring FM to focus
        focused, message = focus_fm()
        if not focused:
            print(f"❌ {message}")
        else:
            print(f"✅ {message}")

            # 3️⃣ Nv to individual training section in FM
            navigate_to_individual_training()
            
            # 4️⃣ Wait for page to load (it sometimes takes a while)
            config = get_config()
            delay = config.get("delay_after_hotkey_in_seconds", 3)
            print(f"⏳ Waiting {delay}s for individual training section to load in FM")
            time.sleep(delay)


if __name__ == "__main__":
    main()

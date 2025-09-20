from is_fm_running import is_fm_running
from focus_fm import focus_fm


def main():
    print("FM23 Auto Praise Players Training started.")

    if is_fm_running():
        print("FM23 IS running")
        focus_fm()
    else:
        print("FM23 IS NOT running")


if __name__ == "__main__":
    main()

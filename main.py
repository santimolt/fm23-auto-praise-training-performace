import psutil

def is_fm_running():
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'] and 'fm' in proc.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False

if __name__ == "__main__":
    if is_fm_running():
        print("FM23 is running!")
    else:
        print("FM23 is not running.")
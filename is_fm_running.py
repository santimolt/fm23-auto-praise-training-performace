import psutil


def is_fm_running():
    for proc in psutil.process_iter(["name"]):
        try:
            if proc.info["name"] and "fm" in proc.info["name"].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False

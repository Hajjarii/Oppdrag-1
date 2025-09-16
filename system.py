import os
import time
import platform
import psutil
 
def get_uptime():
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time
    uptime_str = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))
    return uptime_str
 
def main():
    print("=== Systeminfo ===")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Maskin: {platform.machine()}")
    print(f"Prosessor: {platform.processor()}")
    print(f"Uptime: {get_uptime()}")
    print(f"Nåværende tid: {time.strftime('%Y-%m-%d %H:%M:%S')}")
 
if __name__ == "__main__":
    main()



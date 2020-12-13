# Automatically starts or stops application depending on the connectivity of
# external storage device.

import os
import time
import psutil

app_name = "Plex Media Server"
app_path = "/Applications/Plex Media Server.app"
volume_path = "/Volumes/External"
open_command = "open /Applications/Plex\ Media\ Server.app"
app_killer = "pkill Plex Media Server"


def app_run_checker(process_name):
    for process in psutil.process_iter():
        try:
            if process_name.lower() in process.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied,
                psutil.ZombieProcess):
            pass
    return False;


while True:
    app_exists = os.path.exists(app_path)
    disk_exists = os.path.isdir(volume_path)
    if app_exists is True:
        print("App exists. Ready to continue.")
        if app_run_checker(app_name) and disk_exists is False:
            print("Disk not mounted. Closing Plex.")
            os.system(app_killer)
        elif app_run_checker(app_name) and disk_exists is True:
            print("Everything is connected and running.")
        elif app_run_checker(app_name) is False and disk_exists \
                is True:
            print("Disk exists. Ready to start program.")
            os.system(open_command)
        elif app_run_checker(app_name) is False and disk_exists is False:
            print("App is closed and disk not mounted. Nothing to do.")
    else:
        print("App is missing.")
    time.sleep(10)

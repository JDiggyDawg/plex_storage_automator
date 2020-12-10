# Automatically starts or stops Plex depending on the connectivity of external
# storage device.

import os
import time


def app_checker():
    app_exists = os.path.exists("/Applications/Plex Media Server.app")
    if app_exists is True:
        print("Plex exists. Ready to continue.")
    else:
        print("Plex Media Server is missing.")


def disk_checker_initialize():
    disk_exists = os.path.isdir("/Volumes/LaCie")
    is_running = False  # Need to figure out how to check if app is running
    if is_running is True:
        print("")
    elif disk_exists is True:
        print("Disk exists. Ready to start program.")
        os.system("open /Applications/Plex\ Media\ Server.app")
    else:
        print("Disk not mounted. Closing Plex.")
        os.system("pkill Plex Media Server")


# while True:
    # app_checker()
    # disk_checker_initialize()
    # time.sleep(60)

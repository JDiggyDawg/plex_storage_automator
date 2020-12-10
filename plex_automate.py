# Automatically starts or stops Plex depending on the connectivity of external
# storage device.

import os


def app_checker():
    app_exists = os.path.exists("/Applications/Plex Media Server.app")
    if app_exists is True:
        print("Plex exists. Ready to continue.")
    else:
        print("Plex Media Server is missing.")
        exit()


def disk_checker_initialize():
    disk_exists = os.path.isdir("/Volumes/External")
    if disk_exists is True:
        print("Disk exists. Ready to start program.")
        os.system("open /Applications/Plex\ Media\ Server.app")
    else:
        os.system("pkill Plex Media Server")


app_checker()
disk_checker_initialize()

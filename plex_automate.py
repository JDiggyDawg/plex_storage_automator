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

# os.system("pkill Plex\ Media\ Server")

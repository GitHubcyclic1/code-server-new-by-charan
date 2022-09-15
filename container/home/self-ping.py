#!/usr/bin/env python3
import os
try:
    import requests
except:
    os.system("pip3 install requests")
    import requests
from time import sleep
if __name__ == "__main__":
    if os.getenv("NO_SLEEP") == "1":
        if "APP_NAME" not in os.environ:
            print("APP_NAME unset, terminating...")
            exit()
        app_name = os.getenv("APP_URL")
        while True:
            try:
                requests.get(app_name)
            except:
                print("Ping failed, retrying...")
                try:
                    requests.get(app_name)
                except:
                    print("Cannot ping app, terminating...")
            sleep(10*60)

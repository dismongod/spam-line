import httpx

import threading

import os

x = "" # your bearer token

z = {"content-type":"application/x-www-form-urlencoded","Authorization":"Bearer " + x}

y = "" # message

t = int("") # thread

def a():

    x = httpx.post("https://notify-api.line.me/api/notify",headers=z,data={"message": y})

    s = [200, 201, 204]

    if x.status_code in s:

        print("cool")

    elif x.status_code == 400:

        print(F"rate limit")

try:

    while True:

        if threading.active_count() < t:

            threading.Thread(target=a).start()

except KeyboardInterrupt: os._exit(0)

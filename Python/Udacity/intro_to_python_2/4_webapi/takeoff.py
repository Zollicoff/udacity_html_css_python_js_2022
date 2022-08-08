import os
import requests

os.chdir(r"C:\Users\zolli\IDrive-Sync\Zach\GitHub\GitHub\Python\Udacity\intro_to_python_2\4_webapi")

def takeoff():
    print(TAKEOFF)

try:
    print("3, 2, 1, ...")
    takeoff()
except NameError:
    print("Failed to launch")
    
import os
import requests

os.chdir(r"C:\Users\zolli\IDrive-Sync\Zach\GitHub\GitHub\Python\Udacity\intro_to_python_2\4_webapi")

# use python reuests module to send requests to a web API
r = requests.get('weburl')

if r.status_code == 404:
    print("Page is not found!")
elif r.status_code == 200:
    print("The page has been found!")
    
x = int(input("Enter a number."))
try:
    print(3 / x)
except ZeroDivisionError:
    print("Cant divid by zero!")


# use python try and except blocks to handle disruptive events (called exceptions).



# use a format call JSON to access data from web APIs



# use python dictionaries to structure data in a key-value pairs






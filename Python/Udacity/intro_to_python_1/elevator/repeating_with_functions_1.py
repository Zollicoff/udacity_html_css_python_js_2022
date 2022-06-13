import time

def fav_color():
    response = input("Can you guess what my favorite color is?\n").lower()
    if "purple" in response:
        print("That's right, my favorite color is purple!")
    elif "sandy" in response:
        print("That's not my favorite color, but it's my favorite person!")
        time.sleep(2)
        fav_color()
    else:
        print("Sorry, that's not my favorite color. Try again!")
        time.sleep(2)
        fav_color()

fav_color()
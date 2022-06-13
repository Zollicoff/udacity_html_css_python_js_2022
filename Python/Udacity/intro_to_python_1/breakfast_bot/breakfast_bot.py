# Get input and use it to determine what happens next
# Handle bad input without crashing
# Be flexible with the input the user can enter
# Print messages to the console, with a short pause after each one
# Allow the player to order again if they like

import time

print("Hello! I am Bob, the Breakfast Bot.")
time.sleep(2)
print("Today we have two breakfast meals available.")
time.sleep(2)
print("The first is waffles with strawberries and whipped cream.")
time.sleep(2)
print("The second is sweet potato pancakes with butter and syrup.")
time.sleep(2)
while True:
    response = input("Please place your order. "
                     "Would you like the waffles or pancakes?\n").lower()
    if "waffles" in response:
        print("Okay, waffles it is!")
        time.sleep(2)
        break
    elif "pancakes" in response:
        print("Okay, pancakes it is!")
        time.sleep(2)
        break
    else:
        print("Woah, sorry... I don't understand.")
        time.sleep(2)
print("Your order will be out shortly.")
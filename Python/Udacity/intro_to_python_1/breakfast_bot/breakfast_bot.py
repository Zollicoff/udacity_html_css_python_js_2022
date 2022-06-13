# Get input and use it to determine what happens next
# Handle bad input without crashing
# Be flexible with the input the user can enter
# Print messages to the console, with a short pause after each one
# Allow the player to order again if they like

import time

print("Hello! I am Bob, the Breakfast Bot. \n"
      "Today we have two breakfast meals available. \n"
      "The first is waffles with strawberries and whipped cream. \n"
      "The second is sweet potato pancakes with butter and syrup.")
while True:
    response = input("Please place your order. "
                     "Would you like the waffles or pancakes?\n").lower()
    if "waffles" in response:
        print("Okay, waffles it is!")
        break
    elif "pancakes" in response:
        print("Okay, pancakes it is!")
        break
    else:
        print("Woah, sorry... I don't understand.")

import time

print("Hello! I am Sandy, the Breakfast Bot.")
time.sleep(2)
print("Today we have two breakfast meals available.")
time.sleep(2)
print("The first is waffles with strawberries and whipped cream.")
time.sleep(2)
print("The second is sweet potato pancakes with butter and syrup.")
time.sleep(2)

while True:
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
    time.sleep(2)
    order_again = input("Would you like to place another order? "
                        "Please say 'yes' or 'no'.\n").lower()
    if "yes" in order_again:
        print("Very good, I'm happy to take another order!")
        time.sleep(2)
    elif "no" in order_again:
        print("Okay, goodbye!")
        time.sleep(2)
        break

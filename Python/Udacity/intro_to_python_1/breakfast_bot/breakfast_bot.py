import time

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

print_pause("Hello! I am Sandy, the Breakfast Bot.")
print_pause("Today we have two breakfast meals available.")
print_pause("The first is waffles with strawberries and whipped cream.")
print_pause("The second is sweet potato pancakes with butter and syrup.")

while True:
    while True:
        response = input("Please place your order. "
                         "Would you like the waffles or pancakes?\n").lower()
        if "waffles" in response:
            print_pause("Okay, waffles it is!")
            break
        elif "pancakes" in response:
            print_pause("Okay, pancakes it is!")
            break
        else:
            print_pause("Woah, sorry... I don't understand.")
    print_pause("Your order will be out shortly.")
    while True:
        order_again = input("Would you like to place another order? "
                            "Please say 'yes' or 'no'.\n").lower()
        if "yes" in order_again:
            print_pause("Very good, I'm happy to take another order!")
            break
        elif "no" in order_again:
            print_pause("Okay, goodbye!")
            break
        else:
            print_pause("Woah, sorry... I don't understand.")
    if "no" in order_again:
        break

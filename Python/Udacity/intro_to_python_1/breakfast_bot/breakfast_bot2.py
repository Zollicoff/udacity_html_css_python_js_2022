import time

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            return response
        elif option2 in response:
            return response
        else:
            print_pause("Woah sorry, I don't understand.")

def intro():
    print_pause("Hello! I am Sandy, the Breakfast Bot version 2.0.")
    print_pause("Today we have two breakfast meals available.")
    print_pause("The first is waffles with strawberries and whipped cream.")
    print_pause("The second is sweet potato pancakes with butter and syrup.")

def get_order():
    response = valid_input("Please place your order. "
                           "Would you like the waffles or pancakes?\n",
                           "waffles", "pancakes").lower()
    if "waffles" in response:
        print_pause("Okay, waffles it is!")
    elif "pancakes" in response:
        print_pause("Okay, pancakes it is!")
    print_pause("Your order will be ready shortly.")

def order_again():
    response = input("Would you like to place another order? "
                     "Please say 'yes' or 'no'.\n").lower()
    if "yes" in response:
        print_pause("Very good, I'm happy to take another order!")
        get_order()
    elif "no" in response:
        print_pause("Okay, goodbye!")

def order_breakfast():
    intro()
    get_order()        
    order_again()

order_breakfast()

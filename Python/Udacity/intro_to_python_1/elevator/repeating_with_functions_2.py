import time

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

def green_room():
    print_pause("You are in the green room.")
    choose_room()

def blue_room():
    print_pause("You are in the blue room.")
    choose_room()

def choose_room():
    choice = input("Would you like to go into the green "
                   "room or the blue room?\n").lower()
    if "green" in choice:
        green_room()
    elif "blue" in choice:
        blue_room()
    else:
        print_pause("I don't know what that is.")
        choose_room()

choose_room()
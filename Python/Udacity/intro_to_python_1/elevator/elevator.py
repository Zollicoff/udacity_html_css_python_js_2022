import time
inventory = []

def print_pause(message):
    print(message)
    time.sleep(1)

def intro():
    print_pause("You have just arrived at your new job!")
    print_pause("You are in the elevator.")
    
def where_next():
    print_pause("You head back to the elevator.")
    print_pause("Where would you like to go next?")

def lobby():
    print_pause("You push the button for the first floor.")
    print_pause("After a few moments, you find yourself in the lobby.")
    if "ID card" not in inventory:
        print_pause("The clerk greets you and gives you your ID card.")
        inventory.append("ID card")
    else:
        print_pause("The clerk greets you, but she has already given you your ID card, so there is nothing more to do here now.")
    where_next()
    
def hr():
    print_pause("You push the button for the second floor.")
    print_pause("After a few moments, you find yourself in the human resources department.")
    if "ID card" not in inventory:
        print_pause("The head of HR greets you.")
        print_pause("He has something for you, but says he can't give it to you until you go get your ID card.")
    elif "handbook" not in inventory:
        print_pause("The head of HR Greets you.")
        print_pause("He looks at your ID card and then gives you a copy of the employee handbook.")
        inventory.append("handbook")
    else:
        print_pause("The HR folks are busy at their desks.")
        print_pause("There doesn't seem to be much to do here.")
    where_next()
    
def engineering():
    print_pause("You push the button for the third floor.")
    print_pause("After a few moments, you find yourself in the engineering department.")
    print_pause("This is where you work!")
    if "ID card" not in inventory:
        print_pause("Unfortunately, the door is locked and you can't get in.")
        print_pause("It looks like you need some kind of key card to open the door.")
    else:
        if "handbook" not in inventory:
            print_pause("You use your ID card to open the door.")
            print_pause("Your program manager greets you and tells you that you need to have a copy of the employee handbook in order to start work.")
            print_pause("They scowl when they see that you don't have it, and send you back to the elevator.")
        else:
            print_pause("Fortunately, you already got that from HR!")
            print_pause("Congratulations! You are ready to start your new job as vice president of engineering!")
            exit()
        where_next()

def question():
    print_pause("Please enter the number for the floor you would like to visit.")
    floor == input("1. Lobby \n"
                  "2. Human resources \n"
                  "3. Engineering department \n")
    if "1" in floor:
        lobby()
    elif "2" in floor:
        hr()
    elif "3" in floor:
        engineering()
    else:
        print_pause("I'm sorry, I don't understand that.")
    question()

def elevator():
    intro()
    question()

elevator()
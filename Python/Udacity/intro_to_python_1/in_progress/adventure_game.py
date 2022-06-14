import time
import random


def print_pause(message):
    print(message)
    time.sleep(1)


def random_monster():
    list = ["gorgon", "evil fairy", "troll"]
    return(random.choice(list))


def play_again():
    play_again = input("Would you like to play again? (y/n) \n")
    if play_again == "y":
        print_pause("Excellent! Restarting the game ...")
        adventure_game()
    elif play_again == "n":
        print_pause("Thanks for playing! See you next time.")
        time.sleep(2)
        exit()


def intro(monster):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + monster + " is somewhere around "
                "here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.")
    print("")


def fight_query(monster, inventory):
    fight = input("Would you like to (1) fight or (2) run away? \n")
    if fight == "1":
        if "sword" not in inventory:
            print_pause("You do your best...")
            print_pause("but your dagger is no match for the " + monster + ".")
            print_pause("You have been defeated.")
            play_again()
        else:
            print_pause("As the " + monster + " moves to attack, you "
                        "unsheath your new sword.")
            print_pause("The Sword of Ogoroth shines brightly in your "
                        "hand as you brace yourself for the attack.")
            print_pause("But the " + monster + " takes one look at your "
                        "shiny new toy and runs away!")
            print_pause("You have rid the town of the " + monster + ". You "
                        "are victorious!")
            play_again()
    if fight == "2":
        print_pause("You run back into the field. Luckily, you "
                    "don't seem to have been followed.")
        print("")
        house_or_cave(monster, inventory)


def house(monster, inventory):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens "
                "and out steps a " + monster + ".")
    print_pause("Eep! This is the " + monster + "'s house!")
    print_pause("The " + monster + " attacks you!")
    if "sword" not in inventory:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")
        fight_query(monster, inventory)
    else:
        fight_query(monster, inventory)


def cave(inventory):
    if "sword" not in inventory:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger "
                    "and take the sword with you.")
        inventory.append("sword")
        print_pause("You walk back out to the field.")
        print("")
        house_or_cave(inventory)
    else:
        print_pause("You've been here before, and gotten all the "
                    "good stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        print_pause("")
        house_or_cave(inventory, monster)


def house_or_cave(monster, inventory):
    print_pause("Enter 1 to knock on the door")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    answer = input("(Please enter 1 or 2.) \n")
    if answer == "1":
        house(monster, inventory)
    elif answer == "2":
        cave(inventory)


def adventure_game():
    monster = random_monster()
    inventory = []
    intro(monster)
    house_or_cave(monster, inventory)


adventure_game()

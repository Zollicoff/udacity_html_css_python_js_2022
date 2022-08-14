import random

def random_monster():
    list = ["gorgon", "evil fairy", "troll"]
    return(random.choice(list))
    
print_pause("Rumor has it that a " + random_monster() + " is somewhere around here, and has been terrifying the nearby village.")
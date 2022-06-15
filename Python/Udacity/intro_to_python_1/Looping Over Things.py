message = input("What do you have to say, hm?\n")

for ch in message:
    if ch == ".":
        print("You used a period to end you're sentence!")
    if ch == "!":
        print("Wow, you must be excited because you used an exclamation point to end your sentence!")
    if ch == "?":
        print("You used a question mark at the end of your sentence!")
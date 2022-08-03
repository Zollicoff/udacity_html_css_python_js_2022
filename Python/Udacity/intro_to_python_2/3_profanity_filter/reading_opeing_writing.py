with open("mynewfile.txt", "w") as w:
    w.write("I'm writing this shit in my new fucking file! :D")
with open("mynewfile.txt", "r") as r:
    print(r.read())
    print("I just read from my file!")
def password_check():
    while input("Please enter the password: ") != "swordfish":
        print("Wrong! Try again!")
    print("Okay, come on in!")
    
password_check()
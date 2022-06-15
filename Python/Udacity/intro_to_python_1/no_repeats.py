words = []
while True:
    word = input("Tell me a word: ")
    if word in words:
        print("You told me that word already!")
        break
    words.append(word)

print("I've broken out of the loop!")
print(f"Your words were {words}")
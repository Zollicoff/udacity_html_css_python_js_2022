try:
    r = requests.get("https://www.udacity.com")
except NameError:
    print("Did you forget to import the requests module?")

try:
    print(r.text)
except NameError:
    print("Did you forget to define the r variable?")

string = 'short'

try:
    for letter in range(6):
        print(string[letter])
except IndexError:
    print("Whoops, you have an index error!")

print("Woohoo! You got them all!")

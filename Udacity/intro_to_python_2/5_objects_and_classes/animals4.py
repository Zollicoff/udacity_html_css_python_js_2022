class Dog:

    scientific_name = "Canis lupus familiaris"

    def __init__(self, name):
        self.name = name
        self.woofs = 0

    def speak(self):
        print("Woof!")

    def eat(self, food):
        if food == "biscuit":
            print("Yummy!")
        else:
            print("That's not food!")

    def hear(self, words):
        if self.name in words:
            self.speak()

    def count(self):
        self.woofs += 1
        for bark in range(self.woofs):
            self.speak()

class Cat:

    scientific_name = "Felis silvestris catus"

    def __init__(self, name):
        self.name = name
        self.mood = "neutral"

    def speak(self):
        if self.mood == "angry":
            print("Hiss!")
        elif self.mood == "happy":
            print("Purrrrr")
        else:
            print("Meow.")

    def eat(self, food):
        if food == "fish" or "milk":
            print("Yummy!")
        else:
            print("That's not food!")

    def hear(self, words):
        if self.name in words:
            self.speak()

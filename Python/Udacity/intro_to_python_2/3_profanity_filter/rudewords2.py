rude_words = ["crap", "darn", "heck", "jerk", "poop", "butt", "devil"]

import string
import os

os.chdir(r"C:\Users\zolli\IDrive-Sync\Zach\GitHub\GitHub\Python\Udacity\intro_to_python_2\3_profanity_filter")

def check_line(line):
    rude_count = 0
    words = line.split(" ")
    for word in words:
        word = word.strip(string.punctuation).lower()
        print(f"Word: {word}")
        if word in rude_words:
            rude_count += 1
            print(f"Found rude word: {word}")
    return rude_count

def check_file(filename):
    with open(filename) as myfile:
        rude_count = 0
        for line in myfile:
            rude_count += check_line(line)

    if rude_count == 0:
        print("Congratulations, your file has no rude words.")
        print("At least, no rude words I know.")

if __name__ == '__main__':

    check_file("my_story.txt")




# open file
# write to file loop
#close file
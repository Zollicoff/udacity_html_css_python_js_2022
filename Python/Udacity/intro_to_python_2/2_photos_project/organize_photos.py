import os


def extract_place(filename):
    return filename.split('_')[1]


def make_place_directories(places): # Here's the function definition
    for place in places:
        os.mkdir(place)


os.chdir("Photos") # Make sure you're already in the correct directory via CLI
originals = os.listdir()
places = []
for filename in originals:
    place = extract_place(filename)
    if place not in places: # This is the key change
        places.append(place)

make_place_directories(places) # Don't forget to call the function!
print(os.listdir()) # This is just a temporary line for testing!

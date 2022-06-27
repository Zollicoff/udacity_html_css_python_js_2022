import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir("Photos")

originals = os.listdir()

print(originals)
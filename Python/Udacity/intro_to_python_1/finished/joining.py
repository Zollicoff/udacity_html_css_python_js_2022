# Here is the example you can test it on:
lines = ["Haiku frogs in snow",
         "A limerick came from Nantucket",
         "Tetrametric drum-beats thrumming, Hiawathianic rhythm."]

# Write your function definition here:
def breakify(strings):
    return "<br>".join(strings)

# Then call the function and print the results
print(breakify(lines))
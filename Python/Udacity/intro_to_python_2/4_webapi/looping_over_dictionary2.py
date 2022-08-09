# generic list
favorites = {
    'color': 'purple',
    'number': 42,
    'animal':'turtle',
    'language': 'python'
}

# for keys
# for key in favorites.keys():
#    print(key)

# for values
# for value in favorites.values():
#    print(value)

# for item (key and value)
# for entry in favorites.items():
#    print(entry)

# for key and value separately at the same time
# for key, value in favorites.items():
#    print(key)
#    print(value)

# using key and value
# for key, value in favorites.items():
#    print(f"my favorite {key} is {value}")

list = []
for item in favorites.items():
    list.append(item)

print(list)

def possible_tag(word):
    if word.startswith("<") and word.endswith(">"):
        print(word, "could maybe be an HTML tag")
    else:
        print(word, "is definitely not an HTML tag (but might contain one)")
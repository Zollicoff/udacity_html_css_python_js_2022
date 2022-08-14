import random
import words

def silly_string(nouns, verbs, templates):
    template = random.choice(templates)
    output = []
    position = 0
    while position < len(template):
        if template[position:position + 8] == '{{noun}}':
            output.append(random.choice(nouns))
            position += 8
        elif template[position:position + 8] == '{{verb}}':
            output.append(random.choice(verbs))
            position += 8
        else:
            output.append(template[position])
            position += 1
    return "".join(output)

# To see the results, we need to call the funtion and print what it returns:
print(silly_string(words.nouns, words.verbs, words.templates))
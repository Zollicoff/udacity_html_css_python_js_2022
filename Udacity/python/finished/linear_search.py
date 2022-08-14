def until_dot(s):
    index = 0
    while index < len(s) and s[index] != ".":
        index += 1
    return(s[:index])

print(until_dot("Udacity.com"))
print(until_dot("This is a sentence. This is another."))
print(until_dot("192.168.200.2"))
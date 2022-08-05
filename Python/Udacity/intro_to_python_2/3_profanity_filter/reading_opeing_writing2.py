with open("old_file.txt", "r") as o:
    contents = o.read()
    with open("mynewfile.txt", "w") as w:
        w.write(contents)

with open("mynewfile.txt", "r") as n:
    print(n.read())

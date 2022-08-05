# read text file and write it's contents to 'contents' variable
with open("old_file.txt", "r") as o:
    contents = o.read()
    with open("mynewfile.txt", "w") as w:
        w.write(contents)



# read the new file after replace
with open("mynewfile.txt", "r") as n:
    print(n.read())



# search the file for numbers, *need to change to reference swear words list
with open("textfile1", "w") as w:
    for num in range(31):
        if num % 2 == 0:
            w.write(str(num))
            w.write("\n")



# for replacement

s = s.replace()

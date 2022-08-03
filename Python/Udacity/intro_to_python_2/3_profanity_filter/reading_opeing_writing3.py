with open("textfile1", "w") as w:
    for num in range(31):
        if num % 2 == 0:
            w.write(str(num))
            w.write("\n")


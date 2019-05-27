row = 1
while row <= 10:

    if row <= 5:
        col = 1
        while col <= row:
            print("*", end="")
            col += 1
        row += 1
    else:
        col = 10
        while row < col:
            print("*", end="")
            col -= 1
        row += 1
    print()
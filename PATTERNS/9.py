n = 10
for row in range(1, n + 1):
    for space in range(n - row):
        print("  ", end="")

    for col in range(row, 0, -1):
        print(col, end=" ")

    for col in range(2, row + 1):
        print(col, end=" ")

    print()


original_n = 5
n = 2 * original_n
for row in range(n + 1):
    for col in range(n + 1):
        at_every_index = original_n - min(min(row, col), min(n - row, n - col))
        print(at_every_index, end=" ")
    print()



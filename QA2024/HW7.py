size = int(input('> Enter size of triangle: '))
for i in range(1, size + 1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print("")
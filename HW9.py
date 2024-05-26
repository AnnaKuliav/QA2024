def num_pattern(number):
    if num < 1 or num > 9:
        print("Please put number only in the range 1 to 9.")
        return
    for i in range(1, num + 1):
        for j in range(num - i):
            print(" ", end=" ")
        for j in range(1, i + 1):
            print(j, end=" ")
        for j in range(i - 1, 0, -1):
            print(j, end=" ")
        print()
num = int(input("Enter n: "))
num_pattern(num)







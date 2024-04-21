a = int(input('Number 1: '))
b = int(input('Number 2: '))
c = int(input('Number 3: '))
if a >= b and a >= c:
    print("The maximum number is:", a)
elif b >= c:
    print("The maximum number is:", b)
else:
    print("The maximum number is:", c)
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
by_3_not_5 = []
by_5_not_3 = []
by_3_and_5 = []

for i in list:
    if i % 3 == 0 and i % 5 != 0:
        by_3_not_5.append(i)
    elif i % 5 == 0 and i % 3 != 0:
        by_5_not_3.append(i)
    elif i % 3 == 0 and i % 5 == 0:
        by_3_and_5.append(i)

print(list)
print(by_3_not_5)
print(by_5_not_3)
print(by_3_and_5)
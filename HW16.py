lst = [1, 2, 3, 4, 5]
result = [lst[0]]
for i in range(1, len(lst)):
    average = (lst[i] + lst[i - 1]) / 2
    result.extend([average,lst[i]])
print("lst =", lst)
print("Result:", result)
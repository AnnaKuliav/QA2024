def lstdict(lst):
    result_dict = {}
    for i in range(0, len(lst) - 1, 2):
        result_dict[lst[i]] = lst[i + 1]
    return result_dict

print(lstdict([0, 1, 2, 3]))
print(lstdict(['a', 'A', 'b', 'B', 'c']))
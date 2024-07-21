import re

lst = [1, 2, [3, 4, [5, 6], 7], 8, [9, [10]], 11]
input_line = str(lst)

split_lst = re.split(r'[\[\],]', input_line)
split_lst = [int(item.strip()) for item in split_lst if item.strip().isdigit()]
print(split_lst)
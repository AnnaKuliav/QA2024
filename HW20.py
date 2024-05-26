with open('/Users/annakuliavets/Documents/pythonQA2024/20.1.txt', 'r') as f:
    longest = " "
    for line in f:
        if len(line)>len(longest):
            longest = line
print("Longest line's length= ", len(longest))
print(longest)
data = [1, 2, 3, 4, 5]

def find_second_maximum(lst):
    if len(lst) < 2:
        return None

    first_max = max(lst[0], lst[1])
    second_max = min(lst[0], lst[1])

    for i in range(2, len(lst)):
        if lst[i] > first_max:
            second_max = first_max
            first_max = lst[i]
        elif lst[i] > second_max and lst[i] != first_max:
            second_max = lst[i]
    return second_max

print(find_second_maximum(data))



import random

def get_random_string(length: int) -> str:
    result = []
    for _ in range(length):
        char_type = random.randint(1, 3)
        if char_type == 1:
            result.append(chr(random.randint(48, 57)))
        elif char_type == 2:
            result.append(chr(random.randint(65, 90)))
        else:
            result.append(chr(random.randint(97, 122)))
    return ''.join(result)

 #examples:
print(get_random_string(10))
print(get_random_string(15))
print(get_random_string(20))


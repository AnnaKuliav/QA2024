import random

def generate_password(length: int) -> str:
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    result = []
    for _ in range(length):
        char_type = random.randint(1, 4)
        if char_type == 1:
            result.append(chr(random.randint(48, 57)))
        elif char_type == 2:
            result.append(chr(random.randint(65, 90)))
        elif char_type == 3:
            result.append(chr(random.randint(97, 122)))
        elif char_type == 4:
            special_characters = "!$%&?"
            result.append(random.choice(special_characters))

    return ''.join(result)

print(generate_password(12))
users = [
    {'name': 'Luarvik L. Luarvik', 'age': 17},
    {'name': 'Olaf Andvarafors', 'age': 18},
    {'name': 'Brun Du Barnstokr', 'age': 19}
]
user_names = []
for user in users:
    if user['age'] >= 18:
        user_names.append(user['name'])
print(user_names)
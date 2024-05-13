import re
pattern = '^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
user_id = 'aaa@bbb.ccc'
if re.fullmatch(pattern, user_id):
    print('valid email')
else:
    print('invalid email')
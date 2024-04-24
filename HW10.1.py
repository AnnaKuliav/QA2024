word = input('put word for checking ')
symbol = [' ']
for x in symbol:
    word = word.replace(x,'')
    word = word.lower()
n = word[::-1]
if word == n:
    print("True")
else:
    print("False")



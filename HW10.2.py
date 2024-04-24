word = input('put word for checking ')
symbol = [' ']
for x in symbol:
    word = word.replace(x,'')
    word = word.lower()
s = str(word)
l = len(s)
for i in range(l//2):
    if s[i] != s[-1-i]:
       print("True")
       break
else:
    print("False")

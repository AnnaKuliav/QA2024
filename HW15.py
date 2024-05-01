lst = [2, 4, 6, 2, 1, 1, 9, 4, 6]
MIN = 3
MAX = 6
elements = [x for x in lst if MIN <= x <= MAX]
if elements:
    sum = sum(elements)
    product = 1
    for num in elements:
        product *= num
else:
    sum = None
    product = None

print('lst =', lst)
print('MIN =',MIN)
print('MAX =',MAX)
print("sum =", str(sum)+",","product =", product)
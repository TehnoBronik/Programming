isbn = int(input())
isbn.replace("-", "")
digits = list(map(int, isbn[:-1]))
mult = list(range(len(isbn)), 1, -1)
s = 0
for i in range(len(digits)):
    pr = digits[i] * mult[i]
    s += pr
if s % 11 == 0:
    True
else:
    False

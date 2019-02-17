n = int(input())
p1 = "программист"
p2 = "программиста"
p3 = "программистов"
if 11 <= n % 100 <=19:
    print (n, p3)
elif 1 < n % 10 <= 4:
    print (n, p2)
elif n % 10 == 1:
    print (n, p1)
else:
    print (n, p3)

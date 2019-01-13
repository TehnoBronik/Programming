from math import sqrt
print ("napishite dlinni storon cherez probel")
a, b, c = list(map(float,input().split()))
if a + b > c and a + c > b and b + c > a:
    p=(a+b+c)/2
    s = sqrt(p*(p-a)*(p-b)*(p-c))
    print("ploschad treugolnika so storonamy {} {} {} ravna {}".format(a, b, c, s))
else:
	print("treugolnik ne suschestvuet")

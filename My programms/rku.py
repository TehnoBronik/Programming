from math import*
print ("vvedite koefficents")
a, b, c = list(map(float,input().split()))
diskr=b*b-4*a*c
if diskr<0:
    print("korney net")
elif diskr==0:
    x=-b/(2*a)
    print("odin koren",x)
else:
    x1=(-b+sqrt(diskr))/(2*a)
    x2=(-b-sqrt(diskr))/(2*a)
    print("perviy koren = ", x1," vtoroy koren = ", x2)

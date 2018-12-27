print ("vvedite price soka")
p1=float(input())
print ("vvedite obiom soka v litrah")
v1=float(input())
print ("vvedite price soka po akcii")
p2=float(input())
print ("vvedite obiom soka po akcii v litrah")
v2=float(input())
if p1/v1>p2/v2:
    print ("vigodno")
elif p1/v1<p2/v2:
    print ("nevigodno")

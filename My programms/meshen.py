import random
from datetime import datetime
now = datetime.now()
random.seed(now)
print ("skolko vistrelov?")
print ("")
e=0
x=0
s= int(input())
for i in range (s):
    raz=random.uniform(0, 10)
    if raz<=3:
        x=10
        e=e+10
    elif raz<=5:
        x=5
        e=e+5
    elif raz<=6:
        x=1
        e=e+1
    else:
        x=0
        e=e+0
    print (x  , raz)
print ("")
print (e)

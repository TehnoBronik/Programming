import random
random.seed(42)
s_sq=16
n=1000000
n_p=0
for i in range (n):
    x=random.uniform(0,4)
    y=random.uniform(0,4)
    print (i, x, y)

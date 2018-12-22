import random
import string
random.seed(42)
s_sq=16
n=100000
n_p=0
for i in range (n):
    x=random.uniform(0,1000)
    y=random.uniform(0,1000)
    z=random.uniform(0,1000)
    a=random.choice(string.ascii_letters)
    b=random.choice(string.ascii_letters)
    print (i, z, a, x, b, y)

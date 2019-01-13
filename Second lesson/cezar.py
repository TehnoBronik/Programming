alph=[]
n=97
while n<=122:
    alph=alph+[n]
    n+=1
print(len(alph))
new_alph=[]
i=0
d=2
while i<len(alph):
    new_alph+=[alph[(i+d)%26]]
    i+=1
print (alph)
print (new_alph)

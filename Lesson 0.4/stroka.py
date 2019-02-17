print ("vvedite stroku")
s=str(input())
vse=0
vov_count=0
for i in range (len(s)):
    if s[i] not in [" ", ".",",","!","?"]:
        vse+=1
    if s[i] in ["a","o","e","i","y","u"]:
        vov_count+=1
print ("vsego bukv: {}".format(vse))
print ("glasnyh: {}".format(vov_count))
print ("soglasnyh: {}".format(vse-vov_count))

print ("vvedite chislo")
ch = int (input())
answ = ""
flag = False
if ch<0:
    flag = True
    ch=ch*(-1)
while ch > 1 :
    ost = ch % 2
    ch = ch // 2
    answ = str (ost) + answ
answ = str(ch) + answ
answ = "0000000000000000"[:16 - len(answ)] + answ
answ = answ[:8] + " " + answ[8:]
if flag:
    answ = "1" + answ[1:]
print (answ)

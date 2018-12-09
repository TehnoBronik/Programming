
while True:
    print ("vvedite chislo")
    a= input()
    if a=="stop":
        break
    else:
        if int(a)%2==1:
            print ("chislo nechotnoe")
        elif int(a)%2==0:
            print ("chislo chotnoe")

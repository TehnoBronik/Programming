def fibonach(i):
    if i==1 or i==2:
        return 1
    x1=1
    x2=1
    r=3
    while r<=i:
        r += 1
        answ = x1 + x2
        x1 = x2
        x2 = answ
    return answ

if __name__ == "__main__":
    print ("vvedite nomer chisla fibonachi")
    print()
    n=int(input())
    t=1
    while t<=n:
        print ("{} chislo: {}".format(t, fibonach(t)))
        t+=1
    print()

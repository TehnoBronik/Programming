s = input("vvedite stroku: ")
ps = input("vvedite podstroku: ")
for i in range(0,(len(s)-len(ps)+1)):
    if s[i:i+len(ps)] == ps:
        print("nashli", i)
        break

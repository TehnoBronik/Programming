print ("vvedite viragenie")
a = float(input())
m = input()
b = float(input())
if m == "+":
    print ("otvet =", a + b)
elif m == "-":
    print ("otvet =", a - b)
elif m == "*":
    print ("otvet =", a * b)
elif m == "/":
    if b == 0:
        print ("oshibka: delenie na 0 ne vozmozhno")
    else:
        print ("otvet =", a / b)
elif m == "**":
    print ("otvet =", a ** b)

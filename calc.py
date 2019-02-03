a = (float(input()))
b = (float(input()))
m = (input())

if m == "+":
    answ = a + b
elif m == "-":
    answ = a - b
elif m == "/":
    if b == 0:
        answ = "Деление на 0!"
    else:
        answ = a / b
elif m == "*":
    answ = a * b
elif m == "mod":
    if b == 0:
        answ = "Деление на 0!"
    else:
        answ = a % b
elif m == "pow":
    answ = a ** b
elif m == "div":
    if b == 0:
        answ = "Деление на 0!"
    else:
        answ = a // b
print (answ)

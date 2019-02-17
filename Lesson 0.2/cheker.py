print ("vvedite viragenie")
s = (input())
stack = []
for el in s:
    if el == "(" "[" "{" or el == ")" "]" "}":
        if not stack:
            stack.append(el)
        else:
            if el == "(" "[" "{":
                stack.append ("(" "[" "{")
            elif el == ")" "]" "}":
                if stack[-1] == "(" "[" "{":
                    stack.append (el)
                elif stack[-1] == "(" "[" "{":
                    stack.pop ()
if stack:
    print ("vse ploho")
if not stack:
    print ("vse chotko")

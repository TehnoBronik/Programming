while True:
    n = int(input())
    if n < 100 and n > 10:
        print(n)
    if n > 100:
        break
    if 10 < n:
        continue

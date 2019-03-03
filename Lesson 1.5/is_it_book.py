def is_it_book(isbn):
    isbn = isbn.replace("-", "")
    digits = list(map(int, isbn[:-1]))
    mult = list(range(len(isbn), 1, -1))
    s = 0
    for i in range(len(digits)):
        pr = digits[i] * mult[i]
        s += pr
    print(11 - s%11)
    if (s + int(isbn[-1])) % 11 == 0:
        return True
    else:
        return False
    print(11 - s%11)

if __name__=="__main__":
    isbn = input()
    print (is_it_book(isbn))

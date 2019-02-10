import random
import sort2
n = int(input("vvedite kol-vo"))
A = [i for i in range (1, n+1)]
random.shuffle(A)
print(A)
print(sort2.selectionsort(A))

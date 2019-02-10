def bubblesort(A):
    swapped = True
    for i in range (len(A) - 1):
        for i in range (len(A)-1):
            if not swap:
                break
            swapped = False
            for j in range(len(A)-1-i):
                if A[j] < A[j+1]:
                    swap (A, j, j + 1)
                    swapped = True
            yield A

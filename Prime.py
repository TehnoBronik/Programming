import time

def print_PM(n, print_res=True):
    start_time = time.time()
    All_Nums = [True]*(n+1)
    for i in range(2,n//2):
        if All_Nums[i] == False:
            continue
        else:
            j = 2*i
            while j <= n:
                All_Nums[j] = False
                j += i
    Res = []
    for i in range(2, n+1):
        if All_Nums[i]:
            Res += [i]
    if print_res:
        print(Res)
    return(time.time() - start_time)

def print_PM_by_Roma(y, print_res=True):
    start_time = time.time()
    Res = []
    for j in range(2, y+1):
        for i in range(2, y+1):
            if j % i == 0:
                if (j == i):
                    Res += [j]
                else:
                    break
    if print_res:
        print(Res)
    return(time.time() - start_time)

#n = int(input('Введите число:'))
#print('Эратосфен в ', print_PM_by_Roma(10000, False) / print_PM(10000, False), ' раз быстрее')

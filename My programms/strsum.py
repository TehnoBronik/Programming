l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l3 = []
for i in range(len(l1)):
    sum = l1[i] + l2[i]
    l3.append(sum)
print(l3)

nums = list(map(int, input().split()))
window = int(input())
print("")

def my_max(l):
    m = l[0]
    for i in range(1, len(l)):
        if m < l[i]:
            m = l[i]
    return m



for i in range(len(nums) - window + 1):
    numwin = my_max(nums[i : window + i])
    print(numwin)

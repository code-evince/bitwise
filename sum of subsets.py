
a = list(map(int,input().split()))
S = int(input())
flag = True
for mask in range(1<<len(a)):   # 2^n  where n is length of thr list
    sum = 0
    for i in range(len(a)):
        if(mask & (1<<i)):
            sum+=a[i]
    if(sum == S):
        print("YES")
        flag= False
        break
if(flag):
    print("NO")
#knapsack

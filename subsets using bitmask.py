a = list(map(int,input("the set : ").split()))
 # 2^n  where n is length of thr list
for mask in range(1<<len(a)):
    subset = []
    for i in range(len(a)):
        if(mask & (1<<i)):
            subset.append(a[i])
    print(subset)

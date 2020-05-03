permutations = []
chosen = []
a = list(map(int,input().split()))
def search():
    if len(permutations) == len(a):
        print(permutations)
    else:
        for i in range(len(a)):
            if(chosen[i]==1):
                continue;
            chosen[i]=1
            permutations.append(i)
            search()
            chosen[i]= 0
            permutations.pop()

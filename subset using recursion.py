x = list(map(int,input().split()))
subset =[]
def search(k):
    if(k == len(x)+1):
        print(subset)
    else:
        subset.append(k)
        search(k+1)

        subset.pop()
        search(k+1)
search(1)

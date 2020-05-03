one = list(map(int,input().split()))
two = list(map(int,input().split()))
three = list(map(int,input().split()))
four = list(map(int,input().split()))
five = list(map(int,input().split()))

matrix = [one, two, three,four,five]
for rows in range(5):
    for cols in range(5):
        if (matrix[rows][cols]== 1):
            r,c = rows+1,cols+1

answer = abs(3-r)+ abs(3-c)
print(answer)

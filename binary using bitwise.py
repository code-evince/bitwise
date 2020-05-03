import math
x = int(input("Enter a decimal no. :"))
for i in range(math.ceil(math.log(x,2)+1),-1,-1): #THE DIGITS REQ FOR REPRESENTING A DECIMAL INTO BINARY
    if((x & (1<<i)) !=0):     #  TAKING BITWISE AND (MASK) WITH LEFT SHIFT 1 IF 1 OCCURS ELSE 0
        print(1,end="")
    else:
        print(0,end="")

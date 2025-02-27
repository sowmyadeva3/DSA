n = int(input())
for i in range(1,n+1):
    for space in range(1, n-i+1):
        print(" ",end="")
    for star in range(1,2*i):
        print("*",end="")
    print()
for i in range(1, n):
    for space in range(1,i+1):
        print(" ",end="")
    for star in range(1,(2*n)-((2*i))):
        print("*",end="")
    print()
n = int(input())
for  i in range(n,0,-1):
    #Print space
    for space in range(1,n-i+1):
        print(" ",end="")
    #Print *
    for star in range((2*i)-1,0,-1):
        print("*",end="")
    print()
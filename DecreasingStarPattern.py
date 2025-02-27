#Get n from user
n = int(input())
# Outer loop from 1 to N
for i in range(1,n+1):
    # inner loop from i to n-i
    for j in range(1,n-i+2):
        #print *
        print("*",end=" ")
    print()
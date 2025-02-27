#Get n from user
n = int(input())
# Outer loop from 1 to N
for i in range(1,n+1):
    # inner loop from i to n-i
    for j in range(n-i+1,0,-1):
        #print j
        print(j,end=" ")
    print()
    
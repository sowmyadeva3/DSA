n = int(input())
count = 1
for  i in range(1,n+1):
    for j in range(1,i+1):
        print(count,end=" ")
    print()
    count+=1
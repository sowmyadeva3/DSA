arr = list(map(int,input("Enter array values: ").split()))
n = int(input())
for i in range(0,len(arr)):
    arr[i]+=n
print(arr)
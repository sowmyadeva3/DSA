arr = list(map(int,input("Enter array values: ").split()))
sum = 0
for i in range(0,len(arr)):
    sum += arr[i]
print(sum)
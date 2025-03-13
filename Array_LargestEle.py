arr = [2,3,4,5,6,7,8]
largest = arr[0]
for i in range(1,len(arr)):
    if arr[i] > largest:
        largest = arr[i]
print(largest)
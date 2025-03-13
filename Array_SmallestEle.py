arr = [2,3,4,5,6,7,8]
smallest = arr[0]
for i in range(0,len(arr)):
    if arr[i] < smallest:
        smallest = arr[i]
print(smallest)
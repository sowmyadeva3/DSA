arr = [2,3,4,5,6,7,8]
oddCount, evenCount = 0,0
for i in range(0,len(arr)):
    if arr[i]%2 == 0:
        evenCount+=1
    else:
        oddCount+=1
print(evenCount,oddCount)
import math
sum =0
l,r = 10,20

arr = [1] * (r+1)
print(len(arr))

for i in range(2,int(math.sqrt(r))+1):
    if arr[i]==1:
        for j in range(i*2,r+1,i):
            
            arr[j] = 0

for i in range(l,r+1):
    if arr[i] == 1:
        print(i)
        sum+=i
print(sum)
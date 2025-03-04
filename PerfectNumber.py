import math
sum=1
n=int(input())
for i in range(2,math.isqrt(n)+1):
    if n%i == 0:
        print(i)
        sum=sum+i
        if n//i != i:
            sum=sum+(n//i)
if sum==n:
    print("Perfect number")
else:
    print("Not a perfect number")
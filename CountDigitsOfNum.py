# Get n from user
n = int(input("Enter a number: "))
count = 0
while n>0:
    print("n: "+str(n), n%10)
    count = count+1
    n = n//10
print(count)
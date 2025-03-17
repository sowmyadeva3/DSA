# Returns sum of 0's in a number
def findPower(n,power): 
    if power ==0:
        return 1
    if power ==1:
        return n
    return n* findPower(n,power-1)

  
# Driver code 
n = 20
power = 5
print(findPower(n,power))
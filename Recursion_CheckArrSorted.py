# Returns sum of 0's in a number
def printDivisors(n,i): 
    if i>n:
      return
    if n%i ==0:
       print(i,end=" ")
    printDivisors(n,i+1)

  
# Driver code 
n = 122
printDivisors(n,i=1)
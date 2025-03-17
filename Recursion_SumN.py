# Returns sum of first 
# n natural numbers 
def recurSum(n): 
    if n == 1: 
        return 1 
    return n + recurSum(n - 1) 
  
# Driver code 
n = 5
print(recurSum(n))
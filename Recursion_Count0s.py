# Returns sum of 0's in a number
def recurSumZeroes(n): 
    if n<10:
      if n==0:
        return 1
      else:
        return 0
    if n%10==0:
      
      return 1+ recurSumZeroes(int(n/10))
      
    else:
      
      return recurSumZeroes(int(n/10))
      
  
# Driver code 
n = 203009
print(recurSumZeroes(n))
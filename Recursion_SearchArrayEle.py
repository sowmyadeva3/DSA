# Returns sum of 0's in a number
def recurSumArr(arr,i): 
    if i==len(arr)-1:
      return arr[i]
    
    return arr[i]+ recurSumArr(arr,i+1)
  
# Driver code 
arr = [1,2,3,4,5]
print(recurSumArr(arr,i=0))
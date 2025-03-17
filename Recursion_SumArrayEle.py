# Returns sum of 0's in a number
def recurCheckArrSorted(arr,i): 
    if i==len(arr)-1:
      return True
    if arr[i]>arr[i+1]:
       return False
       
    return recurCheckArrSorted(arr,i+1)
  
# Driver code 
arr = [1,2,8,4,5]
print(recurCheckArrSorted(arr,i=0))
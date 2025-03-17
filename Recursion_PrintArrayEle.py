# Returns sum of 0's in a number
def recurSearchArr(arr,x, i): 
    if i==len(arr):
      return -1
    if arr[i] == x:
       return i
    
    return recurSearchArr(arr,x,i+1)
  
# Driver code 
arr = [1,2,3,4,5,6,76,6]
x= 5
print(recurSearchArr(arr,x,i=0))
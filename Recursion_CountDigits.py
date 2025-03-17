# Returns sum of 0's in a number
def recurPrintArr(arr, i): 
    if i==len(arr):
      return
    print(arr[i],end=" ") 
    recurPrintArr(arr,i+1)
  
# Driver code 
arr = [1,2,3,4,5,6,76,6]
recurPrintArr(arr,i=0)
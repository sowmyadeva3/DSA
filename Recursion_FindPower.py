# Returns sum of 0's in a number
def bubbleSort(arr): 
    for j in range(0,len(arr)-1):
        for i in range(0,len(arr)-1-j):
            if arr[i]>arr[i+1]:
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
    return arr

  
# Driver code 
arr = [8,7,6,5,4,3,2,1]
print(bubbleSort(arr))
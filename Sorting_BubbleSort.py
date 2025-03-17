# Returns sum of 0's in a number
def bubbleSort(arr): 
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while key<arr[j] and j>=0:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
        
    return arr

  
# Driver code 
arr = [8,7,6,5,4,3,2,1]
print(bubbleSort(arr))
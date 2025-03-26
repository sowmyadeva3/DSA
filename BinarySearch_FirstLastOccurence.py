#User function Template for python3


class Solution:
    def binarySearch(self,low,high,condition):
        while low<=high:
            mid=(low+high)//2
            result=condition(mid)
            if result=='found':
                return mid
            elif result=='left':
                high = mid-1
            else:
                low=mid+1
        return -1
    def firstOccurence(self,arr,x):
        def condition(mid):
            if arr[mid]==x:
                if mid>0 and arr[mid-1]==x:
                    return 'left'
                else:
                    return 'found'
            elif arr[mid]>x:
                return 'left'
            else:
                return 'right'
        return self.binarySearch(0,len(arr)-1,condition)
        
    def lastOccurence(self,arr,x):
        def condition(mid):
            if arr[mid]==x:
                if mid<len(arr)-1 and arr[mid+1]==x:
                    return 'right'
                else:
                    return 'found'
            elif arr[mid]>x:
                return 'left'
            else:
                return 'right'
        return self.binarySearch(0,len(arr)-1,condition)
    def find(self, arr, x):
        
        return (self.firstOccurence(arr, x), self.lastOccurence(arr, x))


#{ 
 # Driver Code Starts
t = int(input())  # Number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # Input array for each test case
    x = int(input())  # Element to search for
    ob = Solution()
    ans = ob.find(arr, x)  # Call the find function in the Solution class
    print(*ans)  # Print the result as space-separated values
    print("~")

# } Driver Code Ends
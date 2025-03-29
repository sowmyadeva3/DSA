#User function Template for python3
class Solution:
    def findKRotation(self, arr):
        low= 0
        high = len(arr)-1
        while low < high:
            mid = (low + high) // 2
            
            if arr[mid] > arr[high]:  
                low = mid + 1  # Minimum is in the right half
            else:
                high = mid  # Minimum is in the left half or at mid

        return low


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.findKRotation(arr)
        print(res)
        print("~")
# } Driver Code Ends
#User function Template for python3
class Solution:
    def missingNumber(self, arr):
        arr.sort()
        if arr[0] != 1:  # Edge case: If the first number isn't 1, return 1 immediately
            return 1
        n = len(arr) + 1  # Total count should be n, but one is missing
        if arr[-1] == n - 1:  # If the last element is n-1, the missing number is n
            return n
        low=0
        high=len(arr)-1
        while low<high:
            mid =(low+high)//2
            if arr[mid]==mid+1:
                low=mid+1
            else:
                high=mid

        return low+1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(arr)
    print(s)

    print("~")
# } Driver Code Ends
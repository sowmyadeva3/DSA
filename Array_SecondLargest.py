#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        largest = arr[0]
        secondLargest = -1
        for i in range(1,len(arr)):
            if arr[i]>largest:
                largest=arr[i]
        for i in range(0,len(arr)):
            if arr[i]>secondLargest and arr[i]!=largest:
                secondLargest = arr[i]
        return secondLargest


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends
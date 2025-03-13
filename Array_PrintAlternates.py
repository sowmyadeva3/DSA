#User function Template for python3
class Solution:
    def getAlternates(self, arr):
        ls = []
        for i in range(0, len(arr),2):
            ls.append(arr[i])
        return ls
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    ls = Solution().getAlternates(arr)
    print(" ".join(map(str, ls)))
    print("~")

# } Driver Code Ends
class Solution:
    def findNthTerm(self, n):
        sum=1
        for i in range(2,n+1):
            sum+=i
        return sum
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.findNthTerm(N))
        print("~")

# } Driver Code Ends
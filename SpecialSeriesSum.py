class Solution:
    def sumOfTheSeries (self, n):
        sum = 0
        for i in range(1,n+1):
            sum = sum + (i*(i+1))//2
        return sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.sumOfTheSeries(n))
# } Driver Code Ends
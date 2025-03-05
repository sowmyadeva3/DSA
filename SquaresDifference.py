#User function Template for python3
import math
class Solution:
    def squaresDiff (self, N):
        sumOfSquares = 0
        squareofSum = 0
        for i in range(1,N+1):
            sumOfSquares += int(math.pow(i,2))
            squareofSum += i
        return abs(sumOfSquares-int(math.pow(squareofSum,2)))

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        
        ob = Solution()
        print(ob.squaresDiff(N))
# } Driver Code Ends
#User function Template for python3

class Solution:
    def countSquares(self, n):
        result = 0
        counter = 1
        squareValue = 1
        while  True:
            squareValue = counter * counter
            if squareValue<n:
                result += 1
                counter +=1
            else:
                break
        return result
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.countSquares(N))
        print("~")

# } Driver Code Ends
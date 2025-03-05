#User function Template for python3
import math
class Solution:
    def sumOfFifthPowers(self,N):
        sum = 0
        for i in range(1,N+1):
            sum += int(math.pow(i,5))
        return sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.sumOfFifthPowers(N))
        print("~")
# } Driver Code Ends
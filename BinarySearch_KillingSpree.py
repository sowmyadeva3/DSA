#User function Template for python3
import math
class Solution:
    def killinSpree (self, n):
        low=1
        high=int(math.sqrt(n))
        while low<=high:
            mid=(low+high)//2
            sum= (mid*(mid+1)*((2*mid)+1))//6
            if sum>n:
                high=mid-1
            else:
                low=mid+1
        return high
            




#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ans = ob.killinSpree(N);
        print(ans)




        print("~")
# } Driver Code Ends
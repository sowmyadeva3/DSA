import math
class Solution:
    def gcd(self, a : int, b : int) -> int:
        # code here
        if a<b:
            limit = a
        else:
            limit = b
        gcd = 1
        for i in range(2,limit+1):
            if a%i==0 and b%i==0:
                gcd = i
        return gcd


#{ 
 # Driver Code Starts

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a = int(input())
        
        
        b = int(input())
        
        obj = Solution()
        res = obj.gcd(a, b)
        
        print(res)
        

        print("~")
# } Driver Code Ends
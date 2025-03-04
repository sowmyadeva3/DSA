class Solution:
    def middle(self, a, b, c):
        if (a>b and a<c) or (a>c and a<b):
            return a
        elif (b>a and b<c) or (b>c and b<a):
            return b
        else:
            return c



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A = int(input())
        B = int(input())
        C = int(input())
        ob = Solution()
        print(ob.middle(A, B, C))
        print("~")

# } Driver Code Ends
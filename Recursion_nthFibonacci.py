
class Solution:
    def nthFibonacci(self, n: int) -> int:
        # code here
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return self.nthFibonacci(n-1)+self.nthFibonacci(n-2)
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.nthFibonacci(n)

        print(res)

        print("~")

# } Driver Code Ends
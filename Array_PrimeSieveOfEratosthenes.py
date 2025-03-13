#User function Template for python3
import math
class Solution:
    def sieveOfEratosthenes(self, n):
        ls =[]
    	arr = [1] * (n+1)
    	for i in range(2,int(math.sqrt(n))+1):
    	    if arr[i]==1:
    	        for j in range(i*2,n+1,i):
    	            arr[j] = 0
    	for i in range(2,n+1):
    	    if arr[i] == 1:
    	        ls.append(i)
        return ls
    	


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(n)
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends
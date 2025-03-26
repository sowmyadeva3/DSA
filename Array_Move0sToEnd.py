#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
	    j=0
    	for i in range(0,len(arr)):
    	    if arr[i]!=0:
    	        arr[j]=arr[i]
    	        j+=1
        for i in range(j,len(arr)):
            arr[i]= 0
    	        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
        print("~")
# } Driver Code Ends
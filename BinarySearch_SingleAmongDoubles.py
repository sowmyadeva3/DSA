#User function Template for python3

class Solution:
    def findOnce(self,arr):
        low,high = 0, len(arr)-1
        while low<high:
            mid = (low+high)//2
            if mid%2==1:
                mid-=1
            if arr[mid]==arr[mid+1]:
                low=mid+2
            else:
                high=mid
        return arr[low]
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        # n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.findOnce(arr))
        print("~")

# } Driver Code Ends
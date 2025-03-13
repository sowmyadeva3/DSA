#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
#User function Template for python3

class Solution:
    def get_min_max(self, arr):
        min = arr[0]
        max = arr[0] 
        for i in range(1,len(arr)):
            if arr[i] < min:
                min = arr[i]
            if arr[i] > max:
                max = arr[i]
        return min,max
    


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        mn, mx = ob.get_min_max(arr)
        print(mn, mx)
        t -= 1
        print("~")


# } Driver Code Ends
#User function Template for python3

class Solution:
    # Function to find the maximum element from array arr1 and 
    # the minimum element from array arr2 and return their product.
    def find_multiplication(self, arr1, arr2):
        max,min= arr1[0],arr2[0]
        #find max from arr1
        for i in range(1,len(arr1)):
            if arr1[i]>max:
                max = arr1[i]
        #find min in arr2
        for i in range(1,len(arr2)):
            if arr2[i]<min:
                min = arr2[i]
        return max*min
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.find_multiplication(arr1, arr2)
        print(ans)
        print("~")

# } Driver Code Ends
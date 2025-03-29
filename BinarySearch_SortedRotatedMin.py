#User function Template for python3

class Solution:
    def findMin(self, arr):
        low,high = 0,len(arr)-1
        while low < high:
            mid = (low + high) // 2
            
            if arr[mid] > arr[high]:  
                low = mid + 1  # Minimum is in the right half
            else:
                high = mid  # Minimum is in the left half or at mid

        return arr[low]  


#{ 
 # Driver Code Starts
def main():
    T = int(input())

    while T > 0:
        a = list(map(
            int,
            input().strip().split()))  # Convert input to list of integers
        print(Solution().findMin(a))  # Call findMin with the array 'a'
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
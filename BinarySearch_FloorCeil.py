#User function Template for python3

class Solution:
    # User function Template for Python3

    def binary_search(self, low, high, condition):
        while low <= high:
            mid = (low + high) // 2
            result = condition(mid)
            if result == 'found':
                return [mid, mid]
            elif result == 'left':
                high = mid - 1
            else:
                low = mid + 1
        return [high, low]  # Floor is high, Ceil is low
    
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        def condition(mid):
            if arr[mid] == x:
                return 'found'
            elif arr[mid] < x:
                return 'right'
            else:
                return 'left'
        
        arr.sort()  # Sort the array
        
        # Edge cases
        if x < arr[0]:  
            return [-1, arr[0]]  # No floor, smallest element is the ceil
        if x > arr[-1]:  
            return [arr[-1], -1]  # Largest element is the floor, no ceil

        floor_idx, ceil_idx = self.binary_search(0, len(arr) - 1, condition)

        return [arr[floor_idx] if floor_idx >= 0 else -1, 
                arr[ceil_idx] if ceil_idx < len(arr) else -1]

        #{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        x = int(input())
        arr = list(map(int, input().split()))

        ob = Solution()
        ans = ob.getFloorAndCeil(x, arr)
        print(ans[0], ans[1])
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
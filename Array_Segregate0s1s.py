#User function Template for python3

class Solution:
    def segregate0and1(self, arr):
        left=0
        right=len(arr)-1
        while left<=right:
            if arr[left]==0:
                left+=1
            else:
                temp=arr[left]
                arr[left]=arr[right]
                arr[right]= temp
                right-=1


#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = list(map(int, input().strip().split()))

        obj = Solution()
        obj.segregate0and1(arr)

        print(*arr)

        print("~")

# } Driver Code Ends
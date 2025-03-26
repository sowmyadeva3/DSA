#User function template for Python

class Solution:
    def removeDuplicates(self, arr):
        j = 0
        for i in range(0,len(arr)-1):
            if arr[i]!= arr[i+1]:
                arr[j]= arr[i]
                j+=1
        arr[j]=arr[len(arr)-1]
        return j+1        


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    t = int(data[0])
    line = 1

    solution = Solution()

    for _ in range(t):
        if line < len(data):
            arr = list(map(int, data[line].split()))
            line += 1
            ans = solution.removeDuplicates(arr)
            for i in range(ans):
                print(arr[i], end=" ")
            print()
        print("~")

# } Driver Code Ends
#User function Template for python3

class Solution:
    def segregateElements(self, arr):
        res =[]
        for i in range(0,len(arr)):
            if arr[i]>=0:
                res.append(arr[i])
        for i in range(0,len(arr)):
            if arr[i]<0:
                res.append(arr[i])
        for i in range(0,len(res)):
            arr[i]= res[i]


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.segregateElements(a)
        print(*a)

        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
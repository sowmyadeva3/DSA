#User function Template for python3

class Solution:  
    def unionHelper(self,arr,res):
        for i in range(0,len(arr)):
            flag=True
            for j in range(0,len(res)):
                if arr[i]==res[j]:
                    flag=False
                    break
            if flag:
                res.append(arr[i])
                
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        res = []
        self.unionHelper(a,res)
        self.unionHelper(b,res)
        return len(res)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()

        print(ob.findUnion(a, b))
        print("~")

# } Driver Code Ends
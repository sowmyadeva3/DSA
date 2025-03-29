class Solution:
    def find_height(self,tree,n,k):
        
        tree.sort()
        low,high= 0, tree[-1]
        while low<=high:
            mid=(low+high)//2
            #calculate wood collected with mid
            woodCollected = 0
            for i in range(0,len(tree)):
                if tree[i]>mid:
                    woodCollected +=tree[i]-mid
            if woodCollected == k:
                return mid
            elif woodCollected>k:
                low=mid+1
            else:
                high=mid-1
        return -1
        


#{ 
 # Driver Code Starts

t = int(input())
for _ in range(t):
    n = int(input())
    tree = [ int(x) for x in input().strip().split() ]
    k = int(input())
    ob=Solution()
    print(ob.find_height(tree,n,k))
    print("~")
# } Driver Code Ends
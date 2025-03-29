class Solution:
    def checkCapacity(self,weights,days,capacity):
        currentDay = 1
        currCapacity=0
        for i in range(0,len(weights)):
            if currCapacity+weights[i]>capacity:
                currentDay+=1
                currCapacity=0
            currCapacity+=weights[i]
               
                          
        return currentDay<=days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        totalWeights=0
        for i in range(0,len(weights)):
            totalWeights+=weights[i]
        low=max(weights)
        high = totalWeights
        while low<high:
            mid=(low+high)//2
            if self.checkCapacity(weights,days,mid):
                high=mid
            else:
                low=mid+1
        return low
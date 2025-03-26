class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        k = 0
        for i in range(0,len(nums1)):
            for j in range(0,len(nums2)):
                if nums1[i]==nums2[j]:
                    flag = True
                    for h in range(0,k):
                        if nums1[i]==res[h]:
                            flag = False
                            break
                    if flag:
                        res.append(nums1[i])
                        k+=1
        return res
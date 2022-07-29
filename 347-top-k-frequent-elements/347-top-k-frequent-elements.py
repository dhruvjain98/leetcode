class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
 
        numsSet = set(nums)
        numsSetList = list(numsSet)
        
        res = dict()    # num : count
        for i in numsSetList:
            res[i] = nums.count(i)
        
        resList = sorted(res, key=res.get, reverse = True)
        
        return (resList[0:k])
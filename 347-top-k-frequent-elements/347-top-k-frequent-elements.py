class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # sortNums = sorted(nums)
        
        numsSet = set(nums)
        numsSetList = list(numsSet)
        
        res = dict()    # num : count
        for i in numsSetList:
            res[i] = nums.count(i)
        
        print(res)
        
        # resList = list()
        
        # for key,val in res.items():
        #     resList.append(key)
        
        resList = sorted(res, key=res.get, reverse = True)
            
        # print(resList)
        
        return (resList[0:k])
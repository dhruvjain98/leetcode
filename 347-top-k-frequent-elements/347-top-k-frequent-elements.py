class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
# 
#         numsSet = set(nums)
#         numsSetList = list(numsSet)
#         res = dict()    # num : count
#         for i in numsSetList:
#             res[i] = nums.count(i)
            
#         # print(res.get(-1))
        
#         resList = sorted(res, key=res.get, reverse = True)
        
#         return (resList[0:k])

        # BucketSort
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n,c in count.items():
            freq[c].append(n)
        
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return(res)
        
        
        
        
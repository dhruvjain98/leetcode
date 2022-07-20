class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums) - 1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return ([i,j])
        
        prevMap = {} # val: index
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
                
                
        
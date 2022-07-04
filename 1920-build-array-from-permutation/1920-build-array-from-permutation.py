class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        ans = [] * len(nums)
        
#         n = len(nums)
#         # print(n)
        
#         for i in range(n - 1):
#             ans[i] = nums[nums[i]]
#             print(ans[i])
            
#         return ans
        
        return [nums[i] for i in nums]
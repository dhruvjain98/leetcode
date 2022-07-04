class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [] * 2*n
        ans[0:n] = nums
        ans[n:n*2] = nums
        
        return ans
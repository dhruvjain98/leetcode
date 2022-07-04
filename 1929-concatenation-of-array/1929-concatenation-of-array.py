class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        print (n)
        
        ans = [] * 2*n
        print(len(ans))
        
        ans[0:n] = nums
        
        ans[n:n*2] = nums
        
        print(ans)
        
        return ans
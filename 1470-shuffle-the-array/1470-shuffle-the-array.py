class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        left = 0
        right = n
        res = [0] * len(nums)
        
        for i in range(0, len(nums), 2):
            res[i] += nums[left]
            res[i+1] += nums[right]
            
            left += 1
            right += 1
        
        return res
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        val = 0
        
        for item in operations:
            if '+' in item:
                val += 1
            else:
                val -= 1
        
        return val
                
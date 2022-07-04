class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        val = 0
        
        # for item in operations:
        #     if item[0] == "-" or item[1] == "-":
        #         val -= 1
        #     if item[0] == "+" or item[1] == "+":
        #         val += 1
        
        for item in operations:
            if '+' in item:
                val += 1
            else:
                val -= 1
        
        return val
                
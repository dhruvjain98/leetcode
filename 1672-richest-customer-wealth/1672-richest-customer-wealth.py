class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        return (max(sum(acc) for acc in accounts))
        
#         rich = 0
#         for i in range(len(accounts)):
#             curSum = 0
#             for j in range(len(accounts[1])):
                
#                 curSum += accounts[i][j]
            
#             if curSum > rich:
#                 rich = curSum
        
#         return rich
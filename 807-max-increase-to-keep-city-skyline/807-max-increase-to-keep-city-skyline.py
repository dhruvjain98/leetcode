class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        
        north = [0] * n
        east = [0] * n
        
        for r in range(n):
            maxN = 0
            maxE = 0
            for c in range(n):
                if grid[r][c] > maxN:
                    maxN = grid[r][c]
                
                if grid[c][r] > maxE:
                    maxE = grid[c][r]
            
            north[r] = maxN
            east[r] = maxE
        # print(north)
        # print(east)
            
#         for r in range(n):
#             maxN = 0
#             for c in range(n):
#                 if grid[c][r] > maxN:
#                     maxN = grid[c][r]
            
#             east[r] = maxN
#         # print(east)
        
        
        ans = 0
        for i in range(n):
            for j in range(n):
                if (grid[i][j] < min(north[i], east[j])):
                    ans += min(north[i], east[j]) - grid[i][j]
                    
        return ans
                    
        
        
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        
        north = [0] * n
        east = [0] * n
        
        for r in range(n):
            maxN = 0
            for c in range(n):
                if grid[r][c] > maxN:
                    maxN = grid[r][c]
            
            north[r] = maxN
        # print(north)
            
        for r in range(n):
            maxN = 0
            for c in range(n):
                if grid[c][r] > maxN:
                    maxN = grid[c][r]
            
            east[r] = maxN
        # print(east)
        
        
        ans = 0
        for i in range(n):
            for j in range(n):
                # print("{}, {}: ".format(i, j))
                if (grid[i][j] < min(north[i], east[j])):
                    ans += min(north[i], east[j]) - grid[i][j]
                    # print("{}, {}: {}".format(i,j, ans))
                    
        
        # print(ans)
        return ans
                    
        
        
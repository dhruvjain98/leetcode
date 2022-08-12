class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        count = 0
        print("grid n x m: {} x {}".format(len(grid), len(grid[0])))
        
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count += 1
        
        return count
        
    def dfs(self, grid, i, j):
        
        
        # matx = [[-1,0], [1, 0], [0,-1], [0, 1]]
        
        print("i, j: {}, {}".format(i, j))
        if i<0 or j<0 or i >= len(grid) or j >= len(grid[0]):
            return
        
        elif grid[i][j] == "1":
            grid[i][j] = "0"
            
            
#             for x in range(len(matx)):
#                 for y in range(len(matx[0])):
#                     self.dfs(grid, i+x, j+y)
            
            
            self.dfs(grid, i+1, j)
            self.dfs(grid, i-1, j)
            self.dfs(grid, i, j+1)
            self.dfs(grid, i, j-1)

    
            
    
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        """
        1. Convert unsurrounded regions to T    (O at edges of the board)
        2. Convert surrounded regions to X
        3. Convert T back to O
        """
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            
            board[r][c] = "T"
#             dfs(r+1, c)
#             dfs(r-1, c)
#             dfs(r, c+1)
#             dfs(r, c-1)
            
            
            matx = [[1,0], [-1,0], [0,1], [0,-1]]
            for mat in matx:
                i, j = mat[0], mat[1]
                # print("{}, {}".format(r+mat[0], c+mat[1]))
                dfs(r+i, c+j)
            
            
            
            
            
        for r in range(ROWS):
            for c in range(COLS):
            
                if board[r][c] == "O":
                    if r in [0, ROWS - 1] or c in [0, COLS - 1]:
                        dfs(r, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
            
            
                
            
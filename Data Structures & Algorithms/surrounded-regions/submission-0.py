class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        grid = board
        
        rows = len(grid)
        colm = len(grid[0])

        def dfs(i,j): 

            if 0 <= i < rows and 0 <= j < colm and grid[i][j] == "O":

                grid[i][j] = "F"

                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)

            else: 
                return

        for i in range(0,rows): 

            if grid[i][0] == "O":
                dfs(i,0)
        
        for i in range(0,rows): 
            
            if grid[i][colm-1] == "O":
                dfs(i,colm-1)
        
        for j in range(1,colm-1): 
            
            if grid[0][j] == "O":
                dfs(0,j)

        for j in range(1,colm-1): 
            
            if grid[rows-1][j] == "O":
                dfs(rows-1,j)

        for i in range(0,rows): 
            for j in range(0,colm): 

                if grid[i][j] == "O": 
                    grid[i][j] = "X"

                if grid[i][j] == "F": 
                    grid[i][j] = "O"





from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows = len(grid)  
        cols = len(grid[0])

        que = deque()
        
        

        for i in range(0,rows): 
            for j in range(0,cols): 
                if grid[i][j] == 0:
                    que.append((i,j))
                    

        while que: 

            point = que.popleft()
            

            x = point[0]
            y = point[1]

            if 0 <= x+1 < rows and 0 <= y < cols: 

                if grid[x+1][y] == 2147483647: 
                    
                    grid[x+1][y] = grid[x][y] + 1
                    que.append((x+1,y))

            if 0 <= x < rows and 0 <= y+1 < cols: 

                if grid[x][y+1] == 2147483647: 
                    
                    grid[x][y+1] = grid[x][y] + 1
                    que.append((x,y+1))

            if 0 <= x-1 < rows and 0 <= y < cols: 

                if grid[x-1][y] == 2147483647: 
                    
                    grid[x-1][y] = grid[x][y] + 1
                    que.append((x-1,y))

            if 0 <= x < rows and 0 <= y-1 < cols: 

                if grid[x][y-1] == 2147483647: 
                    
                    grid[x][y-1] = grid[x][y] + 1
                    que.append((x,y-1))

    
                    

            

            
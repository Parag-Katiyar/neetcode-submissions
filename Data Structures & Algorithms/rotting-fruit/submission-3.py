from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        que = deque()
        time = 0 

        for i in range(0,rows): 
            for j in range(0,cols): 
                if grid[i][j] == 2:
                    que.append((i,j))

        

        while que: 

            point = que.popleft()

            x = point[0]
            y = point[1]
             

            if 0 <= x+1 < rows and 0 <= y < cols: 

                if grid[x+1][y] == 1:# or grid[x+1][y] == 2: 
                    
                    grid[x+1][y] = grid[x][y] + 1
                    que.append((x+1,y))
                    time = grid[x][y] -1

            if 0 <= x < rows and 0 <= y+1 < cols: 

                if grid[x][y+1] == 1:# or grid[x][y+1] == 2: 
                    
                    grid[x][y+1] = grid[x][y] + 1
                    que.append((x,y+1))
                    time = grid[x][y] -1

            if 0 <= x-1 < rows and 0 <= y < cols: 

                if grid[x-1][y] == 1:# or grid[x-1][y] == 2:
                    
                    grid[x-1][y] = grid[x][y] + 1
                    que.append((x-1,y))
                    time = grid[x][y] -1 

            if 0 <= x < rows and 0 <= y-1 < cols: 

                if grid[x][y-1] ==1:# or grid[x][y-1] == 2: 
                    
                    grid[x][y-1] = grid[x][y] + 1
                    que.append((x,y-1))
                    time = grid[x][y] -1 

        for i in range(0,rows): 
            for j in range(0,cols): 
                if grid[i][j] == 1:
                    return -1

      
        return time 

    
                    

            

            
            
             


        
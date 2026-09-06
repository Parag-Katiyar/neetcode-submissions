from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows = len(grid)  
        cols = len(grid[0])

        que = deque()
        visited = set()
        

        for i in range(0,rows): 
            for j in range(0,cols): 
                if grid[i][j] == 0:
                    que.append((i,j))
                    visited.add((i,j))

        while que: 

            point = que.popleft()
            

            x = point[0]
            y = point[1]

            if 0 <= x+1 < rows and 0 <= y < cols: 

                if (x+1,y) not in visited and grid[x+1][y] == 2147483647: 
                    visited.add((x+1,y))
                    grid[x+1][y] = grid[x][y] + 1
                    que.append((x+1,y))

            if 0 <= x < rows and 0 <= y+1 < cols: 

                if (x,y+1) not in visited and grid[x][y+1] == 2147483647: 
                    visited.add((x,y+1))
                    grid[x][y+1] = grid[x][y] + 1
                    que.append((x,y+1))

            if 0 <= x-1 < rows and 0 <= y < cols: 

                if (x-1,y) not in visited and grid[x-1][y] == 2147483647: 
                    visited.add((x-1,y))
                    grid[x-1][y] = grid[x][y] + 1
                    que.append((x-1,y))

            if 0 <= x < rows and 0 <= y-1 < cols: 

                if (x,y-1) not in visited and grid[x][y-1] == 2147483647: 
                    visited.add((x,y-1))
                    grid[x][y-1] = grid[x][y] + 1
                    que.append((x,y-1))

    
                    

            

            








        
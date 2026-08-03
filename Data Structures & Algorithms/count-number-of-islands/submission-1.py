def island(i,j,o,visited, leng, wid):

    if i < 0 or i > leng-1 or j < 0 or j > wid-1:
        return

    if (i,j) in visited:
        return

    
    if o[i][j] != "1": 
        return

    visited.add((i,j))

  
    island( i+1,j,o, visited, leng, wid)

    island( i,j+1,o, visited, leng, wid)

    island( i-1,j,o, visited, leng, wid)

    island( i,j-1,o, visited, leng, wid)



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        leng  = len(grid)
        wid = len(grid[0])

        count = 0 

        for i in range (leng): 
            for j in range (wid): 

                if grid[i][j] == "1" and (i,j) not in visited:

                    a = i 
                    b = j 

                    count = count + 1 
                    island(a,b,grid, visited, leng, wid)

        return count

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        area_max = 0
        area = 0  
       

        l1 = len(grid)
        l2 = len(grid[0])

        def areax(i,j):
            
            nonlocal area 
            
            
            if 0 <= i < l1 and 0 <= j < l2: 
                

                if grid[i][j] == 2 or grid[i][j] == 0: 
                    return

                elif grid[i][j] == 1: 
                    area = area + 1 
                    grid[i][j] = 2
                    

                areax(i+1, j)
                areax(i, j+1)
                areax(i-1, j)
                areax(i, j-1)
            return 

        for j in range(0,l2): 
            for i in range(0,l1): 

                areax(i,j)

                if area > area_max: 
                    area_max = area

                area = 0 
            
        return area_max

                



        
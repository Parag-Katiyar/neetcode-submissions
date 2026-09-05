class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        area_max = 0
        l1 = len(grid)
        l2 = len(grid[0])

        def areax(i,j):
        
                
            if 0 <= i < l1 and 0 <= j < l2: 
                

                if grid[i][j] == 2 or grid[i][j] == 0: 
                    return 0

                elif grid[i][j] == 1: 
                    grid[i][j] = 2

                    a1 = areax(i+1, j)
                    a2 = areax(i, j+1)
                    a3 = areax(i-1, j)
                    a4 = areax(i, j-1)

                    return 1 + a1 + a2 + a3 + a4
            return 0 

            

        for j in range(0,l2): 
            for i in range(0,l1): 

                area = areax(i,j)

                if area > area_max: 
                    area_max = area

       
            
        return area_max

                



        
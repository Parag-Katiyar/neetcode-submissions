class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m = len(heights)
        n = len(heights[0])

        map1 = [[0 for _ in range(n)] for _ in range(m)]

        map2 = [[0 for _ in range(n)] for _ in range(m)]

        def mark1(i,j):

            if i < 0 or i >= m or j < 0 or j >= n:
                return 

            if map1[i][j] == 1: 
                return 
            
            map1[i][j] = 1 

            if i+1>=0 and i+1 <m:
                if heights[i+1][j] >= heights[i][j]: 
                    mark1(i+1,j)

            if j+1 >= 0 and j+1 < n:
                if heights[i][j+1] >= heights[i][j]: 
                    mark1(i,j+1)

            if i-1 >= 0 and i-1 < m:
                if heights[i-1][j] >= heights[i][j]: 
                    mark1(i-1,j)

            if j-1 >=0 and j-1 < n:
                if heights[i][j-1] >= heights[i][j]:
                    mark1(i,j-1)

            return 

        def mark2(i,j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 

            if map2[i][j] == 1: 
                return 

            map2[i][j] = 1

            if i+1>=0 and i+1 <m:
                if heights[i+1][j] >= heights[i][j]: 
                    mark2(i+1,j)

            if j+1 >= 0 and j+1 < n:
                if heights[i][j+1] >= heights[i][j]: 
                    mark2(i,j+1)

            if i-1 >= 0 and i-1 < m:
                if heights[i-1][j] >= heights[i][j]: 
                    mark2(i-1,j)

            if j-1 >=0 and j-1 < n:
                if heights[i][j-1] >= heights[i][j]:
                    mark2(i,j-1)

            return 

        #For Pacific 

        for i in range (0,n):
            mark1(0,i)

        for i in range (0,m): 
            mark1(i,0)

        #For Atlantic 
        for i in range (0,n):
            mark2(m-1,i)

        for i in range (0,m): 
            mark2(i,n-1)
        
        answer = []

        for i in range(0,m):
            for j in range (0,n): 
                if map1[i][j] and map2[i][j]:
                    answer.append([i, j])
        
        return answer




        
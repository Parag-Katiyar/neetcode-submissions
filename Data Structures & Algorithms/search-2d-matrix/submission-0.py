class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        start = 0 
        n = len(matrix)
        m = len(matrix[0])

        end = m*n - 1

        middle = (start+ end)//2 

        middle_row = middle//m
        middle_colomn = middle%m

        while start <= end:

            if matrix[middle_row][middle_colomn]  == target: 
                return True
            
            if matrix[middle_row][middle_colomn] < target:
                start = middle + 1
                 

            elif matrix[middle_row][middle_colomn] > target: 
                
                end = middle - 1 

            middle = (start+ end)//2 

            middle_row = middle//m
            middle_colomn = middle%m

        return False


             
        
        
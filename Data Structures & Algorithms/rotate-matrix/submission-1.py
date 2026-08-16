#ALWAYS KEEP IN MIND THE INDEX you have to modify (n//2), (i+1,n)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
# 1. Transpose: Start j at i + 1 so we only swap across the diagonal once
        for i in range(0,n): 
            for j in range(i+1,n): 
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

# 2. Reverse Rows: Stop at n // 2 so we don't undo the horizontal flip
        for i in range(0,n):
            for j in range(0,n//2): 
                matrix[i][j],matrix[i][n-1-j] = matrix[i][n-1-j],matrix[i][j]
        
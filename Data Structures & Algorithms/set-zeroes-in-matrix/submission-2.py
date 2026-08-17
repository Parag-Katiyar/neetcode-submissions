#When you need to store the row and column of an element for a later traversal, and you no longer need that element’s original information, reuse the matrix itself as storage. If you encounter (x, y), store the marker in the corresponding first column and first row: matrix[x][0] = 0 and matrix[0][y] = 0. Later, when you encounter (i, j), simply check matrix[i][0] for the row and matrix[0][j] for the column — both are O(1). This gives you the same easy lookup as a set, but without extra space.

"!!!! So the key pattern is: store the row information in the first column and the column information in the first row, using the matrix itself as memory. !!!!" 

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        r = len(matrix)
        c = len(matrix[0])
        flag1 = 0 
        flag2 = 0 

        for i in range(0,r): 
            if matrix[i][0] == 0: 
                flag1 =1 

        for j in range(0,c):
            if matrix[0][j] == 0: 
                flag2 = 1

        for i in range(1,r):

            for j in range(1,c):
                if matrix[i][j] == 0: 
                    matrix[i][0] = 0
                    matrix[0][j] = 0        

        for i in range(1,r): 
            if matrix[i][0] == 0: 
                matrix[i] = [0]*c 

        for j in range(1,c):
            if matrix[0][j] == 0:
                for i in range(r):
                    matrix[i][j] = 0

        if flag1 == 1: 
            for i in range(r):
                matrix[i][0] = 0

        if flag2 == 1:
            matrix[0] = [0]*c 


        
        
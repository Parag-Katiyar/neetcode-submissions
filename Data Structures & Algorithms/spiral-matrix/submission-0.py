class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        step = 0
        array= []
        r = len(matrix)
        c = len(matrix[0]) 
        

        def spl(step):
             
            if len(array) == r*c: 
                return 


            for i in range(step,c-step):

                
                array.append(matrix[step][i])
                if len(array) == r*c: 
                    return

                


            for j in range(step+1,r-step):

                
                array.append(matrix[j][c-step-1])
                if len(array) ==r*c: 
                    return

                

                

            for k in range(c-step-1-1,step-1,-1):

                array.append(matrix[r-1-step][k]) 
                if len(array) == r*c: 
                    return

                


            for l in range(r-1-1-step,step,-1):

                 
                array.append(matrix[l][step])
                if len(array) == r*c: 
                    return

            spl(step+1) 

        spl(0) 

        return array 
            
        
        

        

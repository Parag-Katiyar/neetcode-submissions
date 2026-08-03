class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0]*len(temperatures) # Zeros list 
        stack = []

        for i,t in enumerate(temperatures): 

            while stack and t > stack[-1][0]: #Stack[-1][0] way to access the elements of the 2 value stack 

                stackT, stackInd = stack.pop() # Getting values form a Stack[x,y]
                res[stackInd] = (i-stackInd)

            stack.append([t,i]) #making a stack contaning 2 values 
            
        return res 



        
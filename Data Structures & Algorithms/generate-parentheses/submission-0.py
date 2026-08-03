def gen(ans,state,count,par,n): 

    if count == 0 and len(state) == 2*n: 
        ans.append("".join(state))
        return

    #if count == 0 and state == []:
        #return


            
    for i in par:
         
        if (len(state) + count) == 2 * n and i == "(": 
            continue

        if count == n and i =="(": 
            continue
        if len(state) == 0 and i ==")": 
            continue
        if count <= 0 and i ==")":
            continue 
            

        if i == "(": 
            count = count +1 
            state.append(i)

        elif i == ")": 
            count = count -1 
            state.append(i)
        
        gen(ans,state,count,par,n)

        if i == "(":
            count = count -1 
        elif i ==")": 
            count = count +1

        state.pop()
        





class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []    
        par = ["(",")"]
        state = []
        stack = []
        count = 0

        gen(ans,state,count,par,n)
        return ans
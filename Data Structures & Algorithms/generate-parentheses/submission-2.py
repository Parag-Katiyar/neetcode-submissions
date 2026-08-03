def gen(ans,state,count,open_used,par,n): 

    if count == 0 and len(state) == 2*n: 
        ans.append("".join(state))
        return

    #if count == 0 and state == []:
        #return


            
    for i in par:

        if open_used ==  n and i == "(": 
            continue
        if count == n and i =="(": 
            continue
        if len(state) == 0 and i ==")": 
            continue
        if count <= 0 and i ==")":
            continue 
            

        if i == "(": 
            count = count +1 
            open_used = open_used + 1
            state.append(i)

        elif i == ")": 
            count = count -1 
            state.append(i)
        
        gen(ans,state,count,open_used,par,n)

        if i == "(":
            count = count -1 
            open_used = open_used -1
        else : 
            count = count +1

        state.pop()
        





class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []    
        par = ["(",")"]
        state = []
        stack = []
        count = 0
        open_used = 0 

        gen(ans,state,count,open_used,par,n)
        return ans
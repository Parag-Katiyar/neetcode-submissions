def func(stack, op): 

    num2 = stack.pop()
    num1 = stack.pop()
    

    if op =="+":
       
        stack.append(num1+num2)
        return 

    if op =="-":
        stack.append(num1-num2)
        return  

    if op =="*":
        stack.append(num1*num2)
        return 


    if op =="/":
        stack.append(int(num1/num2))
        return 


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operations = {"+", "-", "/", "*"}

        l = len(tokens)

        if l == 0: 
            return 0 
        if l==1: 
            return int(tokens[0])


        for i in tokens:

            if i in operations: 
                func(stack,i)
                
                continue
            
            stack.append(int(i))
            
            

        return stack.pop()




        
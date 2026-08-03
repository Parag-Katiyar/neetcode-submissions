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
        operations = ["+", "-", "/", "*"]

        l = len(tokens)

        if l == 0: 
            return 0 
        if l==1: 
            return int(tokens[0])


        i = 0 

        

        while i <l:

            if tokens[i] in operations: 
                func(stack,tokens[i])
                i = i + 1 
                continue
            
            stack.append(int(tokens[i]))
            i = i + 1
            

        return stack.pop()




        
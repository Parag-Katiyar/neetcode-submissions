class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0":
            return "0"

        # num1*num2
        l1 = len(num1)
        l2 = len(num2)

       

        result = [0]*(l1+l2)
        z = 0 

        for i in range(l2-1,-1,-1):
            
            
            for j in range(l1-1,-1,-1):
               
                pointer = (l1 + l2 - 1) - z - (l1 - 1 - j)

                x = int(num2[i])*int(num1[j])
                carry = x//10
                digit = x%10

                result[pointer] = result[pointer] + digit
                
                result[pointer - 1] = result[pointer-1] + carry
            z = z+1

        for i in range(l1 + l2-1, 0,-1): 

            x = result[i]%10 
            carry = result[i]//10
            result[i] = x 
            result[i-1] = result[i-1] + carry
        
        i = 0 


        while result[i] == 0:
            i = i + 1
            
        
        result = result[i:]  

        result = "".join(map(str, result))

        return result






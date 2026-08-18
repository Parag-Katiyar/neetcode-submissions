class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0":
            return "0"

        # num1*num2
        l1 = len(num1)
        l2 = len(num2)

        num1 = num1[::-1]
        num2 = num2[::-1]

        
        result = [0]*(l1+l2)

        for i in range(0,l2):
            
            for j in range(0,l1):
                pointer = j+i

                x = int(num2[i])*int(num1[j])
                carry = x//10
                digit = x%10

                result[pointer] = result[pointer] + digit
                
                result[pointer + 1] = result[pointer+1] + carry

        for i in range(0,l1+l2-1): 
            x = result[i]%10 
            carry = result[i]//10
            result[i] = x 
            result[i+1] = result[i+1] + carry


        while len(result) > 1 and result[-1] == 0:
            result.pop()


        result.reverse()
        result = "".join(map(str, result))

        return result






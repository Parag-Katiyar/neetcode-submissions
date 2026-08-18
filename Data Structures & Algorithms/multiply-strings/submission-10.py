## See the logic of carrying forwar the carry in one go !!!! 
## See how the results are store without complicated indexing !!!!

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
               
                #pointer = (l1 + l2 - 1) - z - (l1 - 1 - j)

                p2 = i + j + 1  # Current position
                p1 = i + j 

                mul = int(num2[i]) * int(num1[j])

                # Combine multiplication with whatever is already sitting at p2
                total = mul + result[p2]

                # Update on the fly (Single Pass!)
                result[p2] = total % 10    # Keep the unit digit here
                result[p1] += total // 10  # Accumulate the carry to the left

                #carry = x//10
                #digit = x%10

                #result[pointer] = result[pointer] + digit
                
                #result[pointer - 1] = result[pointer-1] + carry
           
        
        i = 0 

        while result[i] == 0:
            i = i + 1
            
        #result = result[i:]  

        result = "".join(map(str, result[i:]))

        return result

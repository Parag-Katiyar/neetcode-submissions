class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        l = len(digits)

        if l == 1: 
            if digits[0] == 9: 
                digits[0] = 1
                digits.append(0)
                return digits

        if digits[l-1]<9: 
            digits[l-1] = digits[l-1] + 1 
            return digits

        elif digits[l-1] == 9: 

            digits[l-1] = 0
            i = l-2

            while digits[i] ==9:

                if i == 0: 
                    digits[0] = 1
                    digits.append(0)
                    return digits

                digits[i] = 0
            
                i = i - 1 
                
            digits[i] = digits[i] + 1 

            return digits

            

        
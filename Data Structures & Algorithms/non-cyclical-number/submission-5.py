


class Solution:
    def isHappy(self, n: int) -> bool:
        
        num = n 
        
        s = 0 

        def fn(num): 
            s = 0
            d = 0  
            while num != 0:
                d = num%10
                s = s + d*d
                num = num//10
            return s

        y = fn(num)
        x = n
        if y == 1: 
            return True
                
        while x != y: 

            x = fn(x)
            y = fn(fn(y))

            if x==1 or y ==1: 
                return True

        return False
            

    
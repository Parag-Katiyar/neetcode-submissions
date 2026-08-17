class Solution:
    def isHappy(self, n: int) -> bool:
        
        s1 = 0 
        s2 = 0 
        num = n 
        
        s = 0 

        while num != 0:
            d = num%10
            s = s + d*d
            num = num//10

        if s == 1:
            return True

        y = s
        x = n
                

        while x != y: 

            s1 = 0 
            s2 = 0 

            while x !=0:
                d1 = x%10
                s2 = s2 + d1*d1
                x = x//10

            x = s2
                
            while y !=0:
                d2 = y%10
                s1 = s1 + d2*d2
                y = y//10
                
            y = s1
            s1 = 0 

            while y !=0:
                d2 = y%10
                s1 = s1 + d2*d2
                y = y//10
            
            y = s1

            if x==1 or y ==1: 
                return True

        return False
            

    
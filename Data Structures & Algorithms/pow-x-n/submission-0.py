#O(n) for N step and if we half the N at every step we get the O(logN) !!

"Instead of multiplying x n times, repeatedly halve the exponent. If the exponent is even, square the result of the half exponent; if it is odd, multiply by one extra x. Since the exponent is halved at every step, the time complexity is O(log n). For a negative exponent, use 1/x and make n positive."

class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 1: 
            return x
        if n == -1: 
            return 1/x 
        if n ==0: 
            return 1  

        if n < 0: 
            final = 1/x
            m = abs(n)
        else: 
            final = x 
            m = n 

        
        def Pow(final,m):

            while m>1: 

                if m%2 == 0:
                
                    return Pow(final*final,m//2)

                elif m%2 == 1:
                    x = final
                    return x*Pow(final*final,m//2)
                
            return final
        
        return Pow(final,m)



        
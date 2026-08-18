class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 1. Handle edge case
        if n == 0:
            return 1.0
        
        # 2. Handle negative exponents up front
        m = abs(n)
        if n < 0:
            x = 1 / x
        
        # 3. Core iterative binary exponentiation
        result = 1.0
        current_product = x
        
        while m > 0:
            if m % 2 == 1:
                result *= current_product  # Collect the power if exponent is odd
            
            current_product *= current_product  # Square the base factor (x^1 -> x^2 -> x^4...)
            m //= 2  # Halve the exponent
            
        return result
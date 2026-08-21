class Solution:
    def reverse(self, x: int) -> int:
        # 1. Track the sign and work with the absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        result = 0
        while x > 0:
            # 2. Extract the rightmost base-10 digit
            digit = x % 10
            
            # 3. Push it into the result from the right
            result = (result * 10) + digit
            
            # 4. Move to the next base-10 digit
            x //= 10
            
        # 5. Restore the sign
        result *= sign
        
        # 6. Enforce 32-bit signed integer overflow rules [-2^31, 2^31 - 1]
        if result < -2**31 or result > 2**31 - 1:
            return 0
            
        return result

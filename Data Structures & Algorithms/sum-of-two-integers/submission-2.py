class Solution:
    def getSum(self, a: int, b: int) -> int:
        result = 0
        carry = 0
        
        # Loop exactly 32 times to safely process 32-bit integers
        for i in range(32): 
            da = a & 1 
            db = b & 1 

            if carry == 1:
                # Python's 'not' returns a boolean (True/False). 
                # We use bitwise NOT (~) masked to 1 bit, or an explicit toggle, to keep it as an int.
                digit = 1 if (da == db) else 0  # equivalent to not(da ^ db)
                carry = da | db
            else: 
                digit = da ^ db 
                carry = da & db
            
            # FIX 1: Place the digit at index 'i' instead of shifting the whole result left
            result |= (digit << i)

            # Shift inputs right to check the next bit position
            a >>= 1
            b >>= 1 
          
        # FIX 2: Handle negative numbers (Two's Complement sign-extension)
        if result >= 0x80000000:
            result = ~(result ^ 0xFFFFFFFF)

        return result

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0 
    

        for i in range(0,32):
            bit = n&(1<<i)
            bit = bit >> i
            bit = bit<<(31-i) 
            result = result|bit


        return result
        
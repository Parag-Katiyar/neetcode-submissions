class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0 
    
#Do not try this meathod of shifting in one go like I tried to do 31-2*1 to implement this idea one should first extract and then push it to the 0 position then push to position 31 -1 !!! 
#        for i in range(0,32):
#            bit = n&(1<<i)
#            bit = bit<<(abs(31-2*i)) 
#            result = result|bit
#        return result
        

        for i in range(0,32):
            bit = n&(1<<i)
            bit = bit >> i 
            bit = bit<<(31-i) 
            result = result|bit
        
        return result





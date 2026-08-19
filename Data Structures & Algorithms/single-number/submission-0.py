class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #   x ^ x = 0
        #   x ^ 0 = x

        # list = [2,3,4,3,4] applying XOR on the list is equal to apply XOR on --> 2^3^4^3^4
        # ==> 2^(3^3)^(4^4) due to commutative properties of the XOR !!! 
        # 2^(3^3)^(4^4) --> 2^(0)^(0) = 2^0 = 2 
        #no matter how they are arranged element which does not have duplicate will emerge out

        result = 0  

        for i in range(0, len(nums)): 
            result = result^nums[i]
        return result

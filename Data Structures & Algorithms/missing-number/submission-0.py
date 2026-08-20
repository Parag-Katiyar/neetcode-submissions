class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0 
        n = len(nums)
        for i in range(0,n): 
            result = result ^ i ^ nums[i]

        return result^n 
        
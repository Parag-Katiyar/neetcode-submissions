class Solution:
    def rob(self, nums: List[int]) -> int:
        
        l = len(nums)
        memo = {}

        def rob(index):

            if index >= l: 
                return 0

            if index in memo: 
                return memo[index]

            max_rob_i = max(nums[index] + rob(index+2),rob(index+1))

            memo[index] = max_rob_i

            return max_rob_i
        
        return rob(0)

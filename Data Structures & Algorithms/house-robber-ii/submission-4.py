class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses: List[int]) -> int:
            memo = {}
            
            def dp(index):
                if index >= len(houses):
                    return 0
                if index in memo:
                    return memo[index]
                
                # Option 1: Rob current house. Option 2: Skip current house.
                memo[index] = max(houses[index] + dp(index + 2), dp(index + 1))
                return memo[index]
                
            return dp(0)

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
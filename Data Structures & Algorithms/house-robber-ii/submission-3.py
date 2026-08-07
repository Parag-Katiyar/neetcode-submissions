class Solution:
    def rob(self, nums: List[int]) -> int:
        
        l = len(nums)
        memo = {}
        if l <=3: 
            return max(nums)

        def rob(index):

            if index >= l: 
                return 0

            if index in memo: 
                return memo[index]

            max_rob_i = max(nums[index] + rob(index+2),rob(index+1))

            memo[index] = max_rob_i

            return max_rob_i

        m1 = rob(1)
        nums = nums[0:l-1]
        memo = {}
        l = l-1
        m2 = rob(0)

        return(max(m1,m2))

        
        
      
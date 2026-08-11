class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        final_ans = nums[0]
        sumx = nums[0]
    

        for i in range (1,len(nums)):

            sumx = max(nums[i],sumx+nums[i])

            final_ans = max(final_ans,sumx)

        return final_ans 

            



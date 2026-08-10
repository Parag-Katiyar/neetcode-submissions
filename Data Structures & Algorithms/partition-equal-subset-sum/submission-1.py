class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        sumx = sum(nums)
        l = len(nums)
        memo = {}

        if sumx%2 == 1: 
            return False

        real_sum = sumx/2

        def target(sum_cur, index): 

            if sum_cur == real_sum: 
                return True 

            if sum_cur > real_sum: 
                return False
            
            if (sum_cur,index) in memo: 
                return memo[(sum_cur,index)]
            
            if index >= l-1: 
                return False

            x = target(sum_cur + nums[index+1],index+1)

            y = target(sum_cur,index+1)

            if (sum_cur + nums[index+1],index+1) not in memo: 
                memo[sum_cur + nums[index+1],index+1] = x

            if (sum_cur,index+1) not in memo:
                memo[sum_cur,index+1] = y 

            return x or y 

        return target(0,0)




            
            

            


            
            












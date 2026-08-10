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

            take = target(sum_cur + nums[index+1],index+1)

            skip = target(sum_cur,index+1)

            memo[(sum_cur, index)] = take or skip

            return take or skip

        return target(0,0)




            
            

            


            
            












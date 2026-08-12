class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums) == 1: 
            return True

        jump = nums[0]-1

        if jump < 0: 
            return False
    

        for i in range(1,len(nums)-1): 

            if jump == 0 and nums[i] == 0: 
                return False

            jump = max(nums[i],jump)

            jump = jump-1
        
        if jump >= 0: 
            return True
        else: 
            return False


            
            
             
        
        
        
        
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0 
        end = len(nums) - 1

        if len(nums) == 1:
            if nums[0] == target:
                return 0

            return -1

        #if nums[0] < nums[-1]: 
        #    return nums[0]

        if target >= nums[0]:
            if target == nums[0]: 
                return 0
            region = 1

        elif target <= nums[-1]: 
            if target == nums[-1]: 
                return len(nums) -1 
            region = 2 
        else: 
            return -1
        
        while start<= end:

            curr_region = 0 

            middle = (start + end)//2

            if nums[middle] == target: 
                return middle

            if nums[middle] >= nums[0]:
                curr_region = 1

            elif nums[middle] <= nums[-1]: 
                curr_region = 2 

            
            if curr_region == region:

                if nums[middle] < target: 
                    start = middle + 1  # Always move right if middle is too small
                else: 
                    end = middle - 1


                    #if region ==1: 
                    #    start = middle + 1
                    #elif region == 2: 
                    #    end  = middle -1 
                #elif nums[middle] > target: 
                    #if region == 1: 
                    #    start = middle + 1 #end = middle -1 
                    #if region == 2: 
                    #    end = middle -1  #start = middle + 1
            
            elif curr_region != region: 

                if curr_region == 1: 
                    start = middle + 1
                else: 
                    end = middle - 1
        return -1 



             
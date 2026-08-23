from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0 
        end = len(nums) - 1

        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        # Determine target region
        if target >= nums[0]:
            if target == nums[0]: 
                return 0
            region = 1
        elif target <= nums[-1]: 
            if target == nums[-1]: 
                return len(nums) - 1 
            region = 2 
        else: 
            return -1
        
        while start <= end:
            middle = (start + end) // 2

            if nums[middle] == target: 
                return middle

            # Determine midpoint region
            if nums[middle] >= nums[0]:
                curr_region = 1
            else: 
                curr_region = 2 

            # Step 1: Midpoint and Target are in the same region
            if curr_region == region:
                if nums[middle] < target: 
                    start = middle + 1  # Always move right if middle is too small
                else: 
                    end = middle - 1    # Always move left if middle is too large
            
            # Step 2: Midpoint and Target are in different regions
            else: 
                if curr_region == 1:    # Target is in Reg 2, Mid is in Reg 1 -> Move right
                    start = middle + 1
                else:                   # Target is in Reg 1, Mid is in Reg 2 -> Move left
                    end = middle - 1

        return -1

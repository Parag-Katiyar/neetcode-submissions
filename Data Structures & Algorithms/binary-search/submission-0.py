class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start_i = 0 
        end_i = len(nums) - 1
        middle_i = round((start_i + end_i)//2) 

        while start_i <= end_i:


            if target == nums[middle_i]: 
                return middle_i
            

            if nums[middle_i] > target:
                end_i = middle_i - 1 

            elif nums[middle_i] < target: 
                start_i = middle_i + 1
            
            middle_i = round((start_i + end_i)//2)
        
        return -1
                





        
        
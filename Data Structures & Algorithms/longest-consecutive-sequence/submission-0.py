class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        flag_new = 0 
        flag = 0
        setx = set(nums)

        for i in range(len(nums)):

            flag_new = 0

            if nums[i]-1 not in setx:

                flag_new = flag_new +1 

                x = nums[i]+1

                while x in setx:
                    flag_new = flag_new + 1 

                    x = x + 1
            
            if flag_new > flag:

                flag = flag_new 

        return(flag)












        
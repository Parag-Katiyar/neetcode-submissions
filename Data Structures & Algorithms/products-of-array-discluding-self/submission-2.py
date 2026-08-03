class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = [0]*len(nums)

        flag = 0
        zero_index = 0 

        product = 1

        
        for i in range(len(nums)):

            if nums[i] == 0:

                flag = flag + 1

                zero_index = i 

                if flag >= 2:
                    output = [0]*len(nums)

                    return output 
            if nums[i] != 0:
                product = product*nums[i]

        if flag == 1: 

            output[zero_index] = product
            return output 

        for i in range(len(nums)):
            output[i] = product//nums[i]

        return(output) 












        
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: 
                continue                             
                                                 
                #for loop updates i upon the iteration
                #Therefore do not update i in foor loop rather use 
                #the loop itself to update and find the suitable i 

            y = i + 1 
            z = len(nums) - 1

            while y < z: 

                sum3 = nums[i] + nums[y] + nums[z]

                if sum3 == 0:
                    res.append([nums[i], nums[y], nums[z]])
                    z = z - 1
                    y = y + 1
                    while nums[z] == nums[z+1] and z > y:
                        z = z - 1
                    while nums[y] == nums[y-1] and z >y:
                        y = y+1


                if sum3 > 0:
                    z = z - 1 
                if sum3 < 0:
                    y = y + 1 

                 

        return(res)




 

        
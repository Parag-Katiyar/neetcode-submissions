class Solution:
    def findMin(self, nums: List[int]) -> int:

        start = 0
        end = len(nums) - 1

        if len(nums) == 1: 
            return nums[0]
        if nums[0] < nums[-1]: 
            return nums[0]

        while start<=end: 

            middle = (start+end)//2

            #Inflection_Logic !!

            if nums[middle-1] > nums[middle]: 
                return nums[middle]
            if nums[middle+1] < nums[middle]: 
                return nums[middle+1]

            if nums[middle] > nums[start] and nums[middle] > nums[end]: 
                start = middle+1 

            elif nums[middle] < nums[end] and nums[middle] < nums[start]: 
                end = middle-1

            


#check id middle-1 is greater than middle then you have found it 
#or I shoudl conitnure storing the middle and go with the end = middle -1

        
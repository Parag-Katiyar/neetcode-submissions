class Solution:
    def rob(self, nums: List[int]) -> int:
        
        l = len(nums)
        memo = {}

        def rob(index):

            if index >= l: 
                return 0

            #if index == l-1: #why handleing the last case can backfire because when arry are samll like len ~ 1,2 then l-1 and l-2 does not track correct index index>= l is safe condition 
                
                #return nums[l-1]

            #if index == l-2: 
                
                #return nums[l-2]

            if index in memo: 
                return memo[index]

            for j in [1,0]: 

                if j == 1:
                    t1 = rob(index+2) + nums[index]
                    

                if j == 0: 
                    t2 = rob(index+1)

            max_rob_i = max(t1,t2)
            memo[index] = max_rob_i

            return max_rob_i
        
        return rob(0)





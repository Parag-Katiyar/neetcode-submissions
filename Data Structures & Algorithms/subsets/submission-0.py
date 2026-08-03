def subs(ans,state,nums,index,l):

    #if index == l: 
     #   return

    ans.append(state[:])
    

    for i in range(index,l): 

        state.append(nums[i])

        subs(ans,state,nums,i+1,l)

        state.pop()

 

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        state = []
        index = 0 
        l = len(nums)

        subs(ans,state,nums,index,l)

        return ans

        



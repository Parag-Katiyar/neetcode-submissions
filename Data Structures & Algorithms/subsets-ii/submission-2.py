def subs(ans,state,nums,index,l):

    ans.append(state[:])

    #if index == l: 
    #    return
    
    for i in range(index,l): 

        if i > index and nums[i] == nums[i-1]: 
            continue

        state.append(nums[i])
        subs(ans,state,nums,i+1,l)
        state.pop()

 

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        
        ans = []
        state = []
        index = 0 

        nums.sort()

        l = len(nums)
        subs(ans,state,nums,index,l)

        return ans


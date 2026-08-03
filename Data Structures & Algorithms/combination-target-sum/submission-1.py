def com(state,ans,choices,target,sumx,lenx,index): 
 
    if sumx == target: 
        if state in ans:
            return 
        ans.append(state[:])
        return 

    for i in range(index, lenx):

        if sumx + choices[i] <= target: 
            sumx = sumx + choices[i]
            state.append(choices[i])
        else: 
            continue
        
        com(state,ans,choices,target,sumx,lenx,i)
        sumx = sumx - choices[i] 
        state.pop()
      



class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = []
        state = []
        sumx = 0 
        lenx = len(nums)
        index = 0 
        
        com(state,ans,nums,target,sumx,lenx,index)

        return ans

   
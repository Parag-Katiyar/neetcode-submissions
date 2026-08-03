def per(ans,state,nums,l,count): 

  if count == l: 
    ans.append(state[:])
    return

  for i in nums: 

    if i in state: 
      continue

    state.append(i)
    
    
    per(ans,state,nums,l,count+1)
    state.pop()

    #nums.append(ind,temp)
    

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

      ans = [] 
      state = [] 
      l = len(nums)

      per(ans,state,nums,l,0)

      return ans
def per(ans,state,nums,l,count,visited): 

  if count == l: 
    ans.append(state[:])
    return

  for i in nums: 

    if i in visited:
      continue

    visited.add(i)

    state.append(i)
    
    
    per(ans,state,nums,l,count+1,visited)
    state.pop()
    visited.remove(i)

    #nums.append(ind,temp)
    

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

      ans = [] 
      state = [] 
      l = len(nums)
      visited = set()

      per(ans,state,nums,l,0,visited)

      return ans
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        emt = set()
        for i in nums:
            if i in emt: 
             return True
            emt.add(i)

        return False
        





        
        








        
        
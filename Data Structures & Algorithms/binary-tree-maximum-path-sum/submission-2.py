# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        fsum = float("-inf") 

        def msum(node): 

            nonlocal fsum

            if node is None: 
                return 0

            right_sum = msum(node.right) + node.val
            left_sum = msum(node.left) + node.val 

            arm_max = max(right_sum, left_sum) 
            loc_max = right_sum + left_sum - node.val 

       
            if loc_max > fsum:
                fsum = loc_max
             
            if arm_max > 0: 
                return arm_max
            else: 
                return 0
  
        
        msum(root)

        return fsum

            


















            
        



        












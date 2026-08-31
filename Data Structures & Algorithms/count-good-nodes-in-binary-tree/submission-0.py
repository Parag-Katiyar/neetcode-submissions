# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        res = 0  

        def good(curr_max, node): 

            nonlocal res 

            if node is None: 
                return
            
            if curr_max <= node.val: 

                res = res + 1

                good(node.val, node.right)
                good(node.val, node.left)

            else:
                good(curr_max, node.right)
                good(curr_max, node.left)
            
            return
        
        good(root.val,root)

        return res 
            
            

            









        
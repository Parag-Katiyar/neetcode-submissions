# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        seen_levels = set()
        res = []

        def rview(level,node): 

            nonlocal seen_levels
            nonlocal res
            
            if node is None: 
                return 

            if level not in seen_levels: 
                seen_levels.add(level)
                res.append(node.val)
            
            rview( level + 1, node.right )
            rview( level + 1, node.left )

            return
        rview(0,root)

        return res


            

            








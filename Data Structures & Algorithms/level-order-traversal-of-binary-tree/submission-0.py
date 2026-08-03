# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root == None: 
            return []


        index = 0 

        t = [[]]

        def insert(root,index): 

            if root == None: 
                return

            if index == len(t):
                t.append([])

            t[index].append(root.val)

            insert(root.left, index + 1)
            insert(root.right, index + 1 )

        insert(root, index)
            

        return t


        
        
        
        

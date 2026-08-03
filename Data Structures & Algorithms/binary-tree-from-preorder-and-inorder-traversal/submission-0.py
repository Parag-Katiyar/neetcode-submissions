# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        in_map = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0
        
        # Step 2: Recursive helper function using pointer boundaries
        def array_to_tree(left: int, right: int) -> TreeNode:
            nonlocal pre_idx
            
            # Base case: if there are no elements to construct the subtree
            if left > right:
                return None
            
            # Pick current element from preorder traversal as root
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1
            
            # Split the inorder array into left and right subtrees
            mid = in_map[root_val]
            
            # Recursively build left and right subtrees
            root.left = array_to_tree(left, mid - 1)
            root.right = array_to_tree(mid + 1, right)
            
            return root
            
        return array_to_tree(0, len(inorder) - 1)
        
    




        
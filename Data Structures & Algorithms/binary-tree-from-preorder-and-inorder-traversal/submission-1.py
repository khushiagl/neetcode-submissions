# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root_val = preorder[0]
        indices = {val: idx for idx, val in enumerate(inorder)}
        root_index = indices[root_val]
        root = TreeNode(root_val)
        left_size = len(inorder[:root_index])
        if left_size > 0:
            left_subtree = self.buildTree(preorder[1:left_size + 1], inorder[:root_index])
            
            root.left = left_subtree
        right_size = len(inorder[root_index+1:])  
        if right_size > 0:
            right_subtree = self.buildTree(preorder[left_size+1:], inorder[root_index+1:])
            root.right = right_subtree
        return root    
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root):
        def int_func(root_now):
            if root_now.left and root_now.right:
                if root_now.val==2:
                    return int_func(root_now.left) or int_func(root_now.right)
                return int_func(root_now.left) and int_func(root_now.right)
            if root_now.val==0:
                return False
            return True
        return int_func(root)
        
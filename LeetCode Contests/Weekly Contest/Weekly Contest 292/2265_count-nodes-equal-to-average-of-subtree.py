# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root):
        self.total=0
        def calculate_average(node):
            if node==None:
                return 0,0
            left_addition,left_total=calculate_average(node.left)
            right_addition,right_total=calculate_average(node.right)
            temp=(left_addition+right_addition+node.val)//(left_total+right_total+1)
            if temp==node.val:
                self.total+=1
            return left_addition+right_addition+node.val,left_total+right_total+1
        calculate_average(root)
        return self.total
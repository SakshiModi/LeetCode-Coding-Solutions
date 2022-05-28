# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions):
        setA=set()
        setB=set()
        mainDict={}
        for i,j,k in descriptions:
            setA.add(i)
            setB.add(j)
            if i not in mainDict:
                mainDict[i]={k:j}
            else:
                mainDict[i][k]=j
        setNow=setA-setB
        root=TreeNode(setNow.pop())
        setNow={root}
        while(len(setNow)!=0):
            new_set=set()
            
            for z in setNow:
                if z.val in mainDict:
                    i=mainDict[z.val]
                    if 0 in i:
                        x=TreeNode(i[0])
                        z.right=x
                        new_set.add(x)
                    if 1 in i:
                        y=TreeNode(i[1])
                        z.left=y
                        new_set.add(y)
            setNow=new_set
        return root
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head):
        currNode=head.next
        ans=ListNode()
        result=ans
        value=0
        while(currNode):
            if currNode.val!=0:
                value+=currNode.val
            else:
                if ans.val==0:
                    ans.val=value
                else:
                    ans.next=ListNode(value)
                    ans=ans.next
                value=0
            currNode=currNode.next
        return result
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
        currentPos=head
        while(currentPos!=None):
            val1=currentPos.val
            if(currentPos.next!=None):
                currentPos.val=currentPos.next.val
                currentPos=currentPos.next
                currentPos.val=val1
            currentPos=currentPos.next
        return head
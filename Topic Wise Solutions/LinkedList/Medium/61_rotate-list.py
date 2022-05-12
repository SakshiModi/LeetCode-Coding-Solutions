# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k):
        pos=head
        lenLst=0
        while(pos):
            lenLst+=1
            pos=pos.next
        if lenLst==0:
            return head
        k=k%lenLst
        if k==0:
            return head
        pos=head
        x=0
        while(pos.next):
            if x==lenLst-k-1:
                pos1=pos
            x+=1
            pos=pos.next
        pos.next=head
        head=pos1.next
        pos1.next=None
        return head
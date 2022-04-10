# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        currentPos=head
        listSize=0
        while(currentPos!=None):
            listSize+=1
            currentPos=currentPos.next
        if(listSize==n):
            head=head.next
        else:
            currentPos=head
            delPos=listSize-n
            for i in range(delPos-1):
                currentPos=currentPos.next
            currentPos.next=currentPos.next.next
        return head
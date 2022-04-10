# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1==None and list2!=None:
            return list2
        if list1!=None and list2==None:
            return list1
        if list1==None and list2==None:
            return list1
        if list1.val<list2.val:
            pos1=list1
            pos2=list2
        else:
            pos1=list2
            pos2=list1
        ans=pos1
        while(pos1.next!=None and pos2!=None):
            if pos1.next.val<pos2.val:
                pos1=pos1.next
            else:
                temp=pos1.next
                pos1.next=pos2
                pos2=pos2.next
                pos1=pos1.next
                pos1.next=temp
        if(pos1.next==None):
            pos1.next=pos2
        return ans
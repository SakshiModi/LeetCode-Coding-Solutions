# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        pos1=l1
        pos2=l2
        ans=ListNode()
        pos3=ans
        while(pos1 or pos2):
            if(pos1 and pos2):
                sum=pos1.val+pos2.val+pos3.val
                pos1=pos1.next
                pos2=pos2.next
            elif(pos1):
                sum=pos1.val+pos3.val
                pos1=pos1.next
            elif(pos2):
                sum=pos2.val+pos3.val
                pos2=pos2.next
            pos3.val=sum%10
            temp=sum//10
            if(pos1==None and pos2==None and temp==0):
                pos3.next=None
            else:
                pos3.next=ListNode(temp)                
            pos3=pos3.next
        return ans
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self,head,k,temp):
        currentPos=head
        for i in range(k):
            nextVal=currentPos.next
            currentPos.next=temp
            temp=currentPos
            currentPos=nextVal
        return temp
    def reverseKGroup(self, head,k):
        if k==1:
            return head
        currentPos=head
        listLen=0
        lst=[]
        while(currentPos!=None):
            if(listLen%k==0):
                lst.append(currentPos)
            listLen+=1
            currentPos=currentPos.next
        numberKGroup=listLen//k
        if(listLen%k==0):
            lst.append(None)
        temp=None
        currentPos=head
        temp=lst[-1]
        for x in range(numberKGroup-1,-1,-1):
            temp=self.reverseList(lst[x],k,temp)
            currentPos=currentPos.next
        head=temp
        return head
    
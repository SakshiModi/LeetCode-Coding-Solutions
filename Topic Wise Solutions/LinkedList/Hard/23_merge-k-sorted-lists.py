from queue import PriorityQueue
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Wrapper:
    def __init__(self,node):
        self.node=node
    def __lt__(self,other):
        return self.node.val<other.node.val
class Solution:
    def mergeKLists(self, lists):
        priorQueue=PriorityQueue()
        for givenHead in lists:
            if givenHead:
                priorQueue.put(Wrapper(givenHead))
        head=ptr=ListNode(0)
        while(not priorQueue.empty()):
            wNode=priorQueue.get()
            ptr.next=ListNode(wNode.node.val)
            ptr=ptr.next
            wNode.node=wNode.node.next
            if wNode.node:
                priorQueue.put(wNode)
        return head.next
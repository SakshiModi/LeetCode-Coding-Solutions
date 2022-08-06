from heapq import heappop, heappush, heapify
class Solution:
    def halveArray(self, nums):
        for i in range(len(nums)):
            nums[i]=-nums[i]
        sumAll=sum(nums)
        sumReq=sumAll/2
        heapify(nums)
        count=0
        while(sumReq<0):
            elem=heappop(nums)
            new_elem=elem/2
            sumReq-=new_elem
            heappush(nums,new_elem)
            count+=1
        return count
        
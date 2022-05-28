class Solution:
    def minimalKSum(self, nums, k):
        nums=sorted(list(set(nums)))
        n=len(nums)
        i=0
        sumNow=0
        while(i<n and nums[i]<=k):
            k+=1
            sumNow+=nums[i]
            i+=1
        sumAll=(k*(k+1))//2
        return sumAll-sumNow
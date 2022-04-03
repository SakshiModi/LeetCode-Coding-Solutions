class Solution:
    def triangularSum(self, nums):
        if len(nums)==1:
            return nums[-1]
        flag=len(nums)
        sumNow=0
        while(flag!=1):
            sumNow=0
            lst=[]
            for i in range(flag-1):
                lst.append((nums[i]+nums[i+1])%10)
                sumNow+=lst[-1]
            nums=lst
            flag-=1
        return sumNow
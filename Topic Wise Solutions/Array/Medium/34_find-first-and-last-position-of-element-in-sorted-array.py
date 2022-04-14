class Solution:
    def searchRange(self, nums, target):
        n=len(nums)
        ans=[-1,-1]
        count=0
        for i in range(n):
            if(nums[i]==target):
                if(count==0):
                    ans[0]=i
                    ans[1]=i
                    count+=1
                elif(count==1):
                    ans[1]=i
        return ans
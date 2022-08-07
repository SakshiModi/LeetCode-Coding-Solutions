class Solution:
    def findLonely(self, nums):
        n=len(nums)
        if n==1:
            return nums
        nums=sorted(nums)
        ans=[]
        for i in range(n):
            if i==0:
                if nums[i]==nums[i+1] or nums[i]+1==nums[i+1]:
                    pass
                else:
                    ans.append(nums[i])
            elif i==n-1:
                if nums[i]==nums[i-1] or nums[i]-1==nums[i-1]:
                    pass
                else:
                    ans.append(nums[i])
            else:
                if nums[i]==nums[i-1] or nums[i]==nums[i+1] or nums[i]-1==nums[i-1] or nums[i]+1==nums[i+1]:
                    pass
                else:
                    ans.append(nums[i])
        return ans
class Solution:
    def minDeletion(self, nums):
        ans=0
        m=len(nums)
        i=0
        while(i<m):
            if i%2==0:
                if i+1<m and nums[i]==nums[i+1]:
                    ans+=1
                    nums.pop(i)
                    m-=1
                else:
                    i+=1
            else:
                i+=1
        if m%2!=0:
            ans+=1
        return ans
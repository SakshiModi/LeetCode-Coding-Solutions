class Solution:
    def rearrangeArray(self, nums):
        n=len(nums)
        pos=0
        neg=1
        ans=[]
        for i in range(n):
            ans.append(0)
        i=0
        while(i<n):
            if nums[i]>0:
                ans[pos]=nums[i]
                pos+=2
            else:
                ans[neg]=nums[i]
                neg+=2
            i+=1
        return ans
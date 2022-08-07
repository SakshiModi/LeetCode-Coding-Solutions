class Solution:
    def maxScoreIndices(self, nums):
        n=len(nums)
        ones=nums.count(1)
        zeros=0
        flag=[]
        for i in range(n+1):
            if i==0:
                temp=ones
            elif i==n:
                if nums[i-1]==0:
                    zeros+=1
                temp=zeros
            else:
                if nums[i-1]==0:
                    zeros+=1
                else:
                    ones-=1
                temp=zeros+ones
            flag.append(temp)
        ans=[]
        maxElem=max(flag)
        for i in range(n+1):
            if flag[i]==maxElem:
                ans.append(i)
        return ans
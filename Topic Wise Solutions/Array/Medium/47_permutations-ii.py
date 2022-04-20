class Solution:
    def permuteUnique(self, nums):
        n=len(nums)
        if(n==0):
            return []
        elif(n==1):
            return [nums]
        else:
            ans=[]
            for i in range(n):
                temp=[nums[i]]
                remLst=nums[0:i]+nums[(i+1):n]
                for j in self.permuteUnique(remLst):
                    if(temp+j not in ans):
                        ans.append(temp+j)
            return ans

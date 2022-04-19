class Solution:
    def permute(self, nums):
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
                for j in self.permute(remLst):
                    ans.append(temp+j)
            return ans
if __name__=="__main__":
    sol=Solution()
    nums=[1,2,3]
    print(sol.permute(nums))
    nums = [0,1]
    print(sol.permute(nums))
    nums = [1]
    print(sol.permute(nums))
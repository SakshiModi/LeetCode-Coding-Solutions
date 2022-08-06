class Solution:
    def zeroFilledSubarray(self, nums):
        n=len(nums)
        i=1
        if nums[0]==0:
            stack=[1]
        else:
            stack=[0]
        while(i<n):
            if stack[-1]==0:
                if nums[i]==0:
                    stack.append(1)
            else:
                if nums[i]==0:
                    stack[-1]+=1
                else:
                    stack.append(0)
            i+=1
        ans=0
        for i in stack:
            if i!=0:
                ans+=(i*(i+1))//2
        return ans
        
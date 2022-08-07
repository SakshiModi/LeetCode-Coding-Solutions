class Solution:
    def sortEvenOdd(self, nums):
        n=len(nums)
        odd=[]
        even=[]
        for i in range(n):
            if i%2==1:
                odd.append(nums[i])
            else:
                even.append(nums[i])
        odd=sorted(odd,reverse=True)
        even=sorted(even)
        ans=[]
        for i,j in zip(odd,even):
            ans.extend([j,i])
        if len(even)>len(odd):
            ans.append(even[-1])
        return ans
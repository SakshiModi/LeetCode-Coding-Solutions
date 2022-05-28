class Solution:
    def minimumAverageDifference(self, nums):
        n=len(nums)
        if n==1:
            return 0
        a=nums[0]
        b=sum(nums[1:])
        ans=0
        val=abs(a-(b//(n-1)))
        for i in range(1,n-1):
            a+=nums[i]
            b-=nums[i]
            c=a//(i+1)
            d=b//(n-i-1)
            temp=abs(c-d)
            if temp<val:
                ans=i
                val=temp
        temp=abs(sum(nums)//n)
        if temp<val:
            ans=n-1
            val=temp
        return ans
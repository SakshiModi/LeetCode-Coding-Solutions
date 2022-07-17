class Solution:
    def gcd_of_2_num(self,n1,n2):
        while(n2):
            n1,n2=n2,n1%n2
        return n1
    def minOperations(self, nums, numsDivide):
        n=len(numsDivide)
        if n==1:
            gcd=numsDivide[0]
        else:
            gcd=self.gcd_of_2_num(numsDivide[0],numsDivide[1])
            for i in range(2,n):
                gcd=self.gcd_of_2_num(numsDivide[i],gcd)
        nums=sorted(nums)
        m=len(nums)
        ans=0
        while(ans<m):
            if gcd%nums[ans]==0:
                return ans
            ans+=1
        return -1
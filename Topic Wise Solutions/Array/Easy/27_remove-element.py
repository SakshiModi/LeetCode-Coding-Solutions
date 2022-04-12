class Solution:
    def removeElement(self, nums, val):
        i=0
        n=len(nums)
        while(i<n):
            if(nums[i]==val):
                n=n-1
                flag=nums[n]
                nums[n]=nums[i]
                nums[i]=flag
                i=i-1
            i=i+1
        return len(nums[0:n])
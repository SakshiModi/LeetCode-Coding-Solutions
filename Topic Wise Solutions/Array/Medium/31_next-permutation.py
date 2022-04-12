class Solution:
    def nextPermutation(self, nums: List[int]):
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if n>1:
            flag=-1
            for i in range(n-2,-1,-1):
                if nums[i+1]>nums[i]:
                    flag=i
                    break

            if flag==-1:
                nums.reverse()
            else:
                for j in range(flag+1,n):
                    if nums[j]>nums[flag]:
                        temp=j
                nums[flag],nums[temp]=nums[temp],nums[flag]
                nums[flag+1:]=nums[flag+1:][::-1]

                
class Solution:
    def search(self, nums,target):
        i=0
        while(0-len(nums)<=i and i<len(nums)):
            if nums[i]==target:
                if i<0:
                    i=len(nums)+i
                return i
            elif nums[i]>target:
                i=i-1
                if 0-len(nums)<=i and i<len(nums):
                    if nums[i]==target:
                        if i<0:
                            i=len(nums)+i
                        return i
                    elif nums[i]<target:
                        return -1
            elif nums[i]<target:
                i=i+1
                if 0-len(nums)<=i and i<len(nums):
                    if nums[i]==target:
                        if i<0:
                            i=len(nums)+i
                        return i
                    elif nums[i]>target:
                        return -1
        return -1
    
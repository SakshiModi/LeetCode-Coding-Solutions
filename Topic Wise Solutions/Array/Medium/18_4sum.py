class Solution:
    def twoSum(self,nums,target):
        n=len(nums)
        ptr1=0
        ptr2=n-1
        ans=[]
        while(ptr1<ptr2):
            if(nums[ptr1]+nums[ptr2]<target):
                ptr1+=1
                while(ptr1<n and nums[ptr1-1]==nums[ptr1]):
                    ptr1+=1
            elif(nums[ptr1]+nums[ptr2]>target):
                ptr2-=1
                while(ptr2>=0 and nums[ptr2+1]==nums[ptr2]):
                    ptr2-=1
            else:
                ans.append([nums[ptr1],nums[ptr2]])
                ptr1+=1
                while(ptr1<n and nums[ptr1-1]==nums[ptr1]):
                    ptr1+=1
                ptr2-=1
                while(ptr2>=0 and nums[ptr2+1]==nums[ptr2]):
                    ptr2-=1
        return ans
    def threeSum(self, nums,target):
        n=len(nums)
        ans=[]
        i=0
        while(i<n-2):
            lst=self.twoSum(nums[i+1:],target-nums[i])
            if(len(lst)!=0):
                for j in lst:
                    j.append(nums[i])
            ans.extend(lst)
            i+=1
            while(i<n-2 and nums[i-1]==nums[i]):
                i+=1
        return ans
    def fourSum(self, nums, target):
        n=len(nums)
        nums=sorted(nums)
        ans=[]
        i=0
        while(i<n-3):
            lst=self.threeSum(nums[i+1:],target-nums[i])
            if(len(lst)!=0):
                for j in lst:
                    j.append(nums[i])
            ans.extend(lst)
            i+=1
            while(i<n-3 and nums[i-1]==nums[i]):
                i+=1
        return ans
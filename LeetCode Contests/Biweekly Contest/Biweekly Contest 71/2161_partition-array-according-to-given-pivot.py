class Solution:
    def pivotArray(self, nums, pivot):
        ans=[]
        temp1=[]
        temp2=[]
        for i in nums:
            if i<pivot:
                ans.append(i)
            elif i==pivot:
                temp1.append(i)
            elif i>pivot:
                temp2.append(i)
        ans.extend(temp1)
        ans.extend(temp2)
        return ans
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m=len(nums1)
        n=len(nums2)
        if m>0 and n>0:
            newLst=[]
            x=0
            for i in nums1:
                while x<n and nums2[x]<i:
                    newLst.append(nums2[x])
                    x+=1
                newLst.append(i)
            newLst+=nums2[x:]
            newLen=m+n
        elif m>0 and n==0:
            newLst=nums1
            newLen=m
        elif m==0 and n>0:
            newLst=nums2
            newLen=n
        mid=newLen//2
        if (newLen)%2==0:
            return (newLst[mid]+newLst[mid-1])/2
        else:
            return newLst[mid]
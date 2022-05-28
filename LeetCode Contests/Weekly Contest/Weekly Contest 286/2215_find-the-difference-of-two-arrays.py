class Solution:
    def findDifference(self, nums1, nums2):
        a=set(nums1)
        b=set(nums2)
        ans=[list(a-b),list(b-a)]
        return ans
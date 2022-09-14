class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sumAll=set()
        for i in range(len(nums)-1):
            sumNow=sum(nums[i:i+2])
            if sumNow in sumAll:
                return True
            sumAll.add(sumNow)
        return False
            
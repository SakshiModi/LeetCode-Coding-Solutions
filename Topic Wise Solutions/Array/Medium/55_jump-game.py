class Solution:
    def canJump(self, nums):
        n=len(nums)-1
        if(n==0):
            return True
        reachingIndex=0
        for i in range(n):
            bestPos=nums[i]+i
            if(i<=reachingIndex):
                reachingIndex=max(bestPos,reachingIndex)
                if(reachingIndex>=n):
                    return True
            else:
                break
        return False
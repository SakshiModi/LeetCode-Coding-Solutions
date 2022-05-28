class Solution:
    def countPairs(self, nums, k):
        freqDict={}
        n=len(nums)
        for i in range(n):
            if nums[i] in freqDict:
                freqDict[nums[i]].append(i)
            else:
                freqDict[nums[i]]=[i]
        count=0
        for i,j in freqDict.items():
            for ki in range(0,len(j)-1):
                for li in range(ki+1,len(j)):
                    if (j[ki]*j[li])%k==0:
                        count+=1
        return count
                
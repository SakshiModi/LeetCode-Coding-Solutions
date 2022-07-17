class Solution:
    def numberOfPairs(self, nums):
        freq={}
        ans=[0,0]
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        for i in freq.values():
            ans[0]+=i//2
            ans[1]+=i%2
        return ans
                
class Solution:
    def mostFrequent(self, nums, key):
        n=len(nums)
        freq={}
        for i in range(n-1):
            if nums[i]==key:
                if nums[i+1] not in freq:
                    freq[nums[i+1]]=1
                else:
                    freq[nums[i+1]]+=1
        ans=list(freq.keys())[0]
        ans_val=freq[ans]
        
        for k,vals in freq.items():
            if ans_val<vals:
                ans=k
                ans_val=vals
        return ans
            
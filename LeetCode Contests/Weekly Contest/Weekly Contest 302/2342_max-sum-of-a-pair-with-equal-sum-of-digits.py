class Solution:
    def sum_of_digits(self,num):
        sum_now=0
        while(num>0):
            sum_now+=num%10
            num//=10
        return sum_now
    def maximumSum(self, nums):
        freq={}
        ans=-1
        for num in nums:
            sum_now=self.sum_of_digits(num)
            if sum_now not in freq:
                freq[sum_now]=[num]
            else:
                freq[sum_now].append(num)
        for value in freq.values():
            if len(value)>=2:
                value=sorted(value)
                ans=max(ans,value[-2]+value[-1])
        return ans
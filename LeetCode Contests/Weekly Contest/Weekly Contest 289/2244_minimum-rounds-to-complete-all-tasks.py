class Solution:
    def minimumRounds(self, tasks):
        freq={}
        for i in tasks:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        ans=0
        for k,v in freq.items():
            if v==1:
                return -1
            if v%3==0:
                ans+=(v//3)
            else:
                ans+=(v//3)+1
        return ans
            
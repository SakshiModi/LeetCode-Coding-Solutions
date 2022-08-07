class Solution:
    def minSteps(self, s, t):
        freq1={}
        freq2={}
        for i in s:
            if i in freq1:
                freq1[i]+=1
            else:
                freq1[i]=1
        for i in t:
            if i in freq1:
                freq1[i]-=1
                if freq1[i]==0:
                    freq1.pop(i)
            elif i in freq2: 
                freq2[i]+=1
            else:
                freq2[i]=1
        ans=0
        for _,v in freq1.items():
            ans+=v
        for _,v in freq2.items():
            ans+=v
        return ans
        
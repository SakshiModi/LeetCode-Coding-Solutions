class Solution:
    def divideString(self, s, k, fill):
        i=0
        n=len(s)
        ans=[]
        start=0
        end=k
        while(i<n):
            x=s[start:end]
            if(len(x)<k):
                y=k-len(x)
                while(y!=0):
                    x+=fill
                    y-=1
            ans.append(x)
            start+=k
            end+=k
            i+=k
        return ans
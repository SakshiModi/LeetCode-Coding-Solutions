class Solution:
    def countAsterisks(self, s):
        flag=0
        n=len(s)
        i=0
        ans=0
        while(i<n):
            if s[i]=="|" and flag==0:
                flag=1
            elif s[i]=="|" and flag==1:
                flag=0
            elif s[i]=="*" and flag==0:
                ans+=1
            i+=1
        return ans
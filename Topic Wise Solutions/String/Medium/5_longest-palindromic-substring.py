class Solution:
    def longestPalindrome(self, s):
        n=len(s)
        ans=s[0]
        flag=''
        for i in range(0,n):
            prev=i-1
            nxt=i+1
            prevCount,nxtCount,bothCount=1,1,1
            while(prev>=0 and prevCount==1):
                if(s[prev]==s[i]):
                    flag=s[prev:(i+1)]
                    prev=prev-1
                else:
                    prevCount=0
            while(nxt<n and nxtCount==1):
                if(s[nxt]==s[i]):
                    flag=s[i:(nxt+1)]
                    nxt=nxt+1
                else:
                    nxtCount=0
            while(prev>=0 and nxt<n and bothCount==1):
                if(s[prev]==s[nxt]):
                    flag=s[prev:(nxt+1)]
                    prev=prev-1
                    nxt=nxt+1
                else:
                    bothCount=0
            if(len(flag)>len(ans)):
                ans=flag      
        return ans
class Solution:
    def findBinary(self,num):
        if num==0:
            return "0"
        st=""
        while(num>1):
            st=str(num%2)+st
            num=num//2
        return "1"+st
    def minBitFlips(self, start, goal):
        x=self.findBinary(start)
        y=self.findBinary(goal)
        m=len(x)
        n=len(y)
        if m>n:
            y="0"*(m-n)+y
        elif n>m:
            x="0"*(n-m)+x
        ans=0
        for a,b in zip(x,y):
            if a!=b:
                ans+=1
        return ans
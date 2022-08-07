class Solution:
    def minMoves(self, target, maxDoubles):
        if maxDoubles==0:
            return target-1
        ans=0
        if target==1 or target==2:
            return target-1
        while(target>=2 and maxDoubles>0):
            if target%2==1:
                target-=1
                target=target//2
                maxDoubles-=1
                ans+=2
            else:
                target=target//2
                ans+=1
                maxDoubles-=1
        return ans+target-1
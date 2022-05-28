class Solution:
    def waysToBuyPensPencils(self, total, cost1, cost2):
        pens=total//cost1
        ans=0
        for i in range(pens+1):
            ans+=((total-(i*cost1))//cost2)+1
        return ans
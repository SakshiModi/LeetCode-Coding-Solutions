class Solution:
    def minimumCost(self, cost):
        cost=sorted(cost,reverse=True)
        n=len(cost)
        ans=0
        for i in range(n):
            if i%3==0 or i%3==1:
                ans+=cost[i]
        return ans
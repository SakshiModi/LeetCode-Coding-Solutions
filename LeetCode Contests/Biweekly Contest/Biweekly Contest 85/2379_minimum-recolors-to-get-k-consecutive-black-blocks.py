class Solution:
    def minimumRecolors(self, blocks, k):
        i=0
        n=len(blocks)
        ans=len(blocks)
        while(i<n-k+1):
            count=0
            for j in range(k):
                if blocks[i+j]=="W":
                    count+=1
            ans=min(ans,count)
            i+=1
        return ans
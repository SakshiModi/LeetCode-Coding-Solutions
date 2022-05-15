class Solution:
    def maxConsecutive(self, bottom, top, special):
        special.append(bottom-1)
        special.append(top+1)
        special=sorted(special)
        ans=0
        n=len(special)
        for i in range(n-1):
            ans=max(ans,special[i+1]-special[i]-1)
        return ans
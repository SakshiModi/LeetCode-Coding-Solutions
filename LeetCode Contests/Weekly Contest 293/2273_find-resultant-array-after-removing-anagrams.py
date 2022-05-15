class Solution:
    def removeAnagrams(self, words):
        ans=[]
        for i in words:
            if len(ans)!=0 and sorted(ans[-1])==sorted(i):
                continue
            else:
                ans.append(i)
        return ans
class Solution:
    def countPrefixes(self, words, s):
        count=0
        for i in words:
            if s.startswith(i):
                count+=1
        return count
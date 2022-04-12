class Solution:
    def strStr(self, haystack, needle):
        if(needle in haystack):
            ans=haystack.index(needle)
        else:
            ans=-1
        return ans
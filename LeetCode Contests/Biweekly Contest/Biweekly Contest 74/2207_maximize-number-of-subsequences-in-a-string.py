class Solution:
    def find_Subsequence(self,string,s1,s2):
        count=0
        ans=0
        if s1==s2:
            count=string.count(s1)
            res=(count*(count-1))//2
            return res
        for i in string:
            if i==s1:
                count+=1
            elif i==s2:
                ans+=count
        return ans
    def maximumSubsequenceCount(self, text, pattern):
        return max(self.find_Subsequence(pattern[0]+text,pattern[0],pattern[1]),self.find_Subsequence(text+pattern[1],pattern[0],pattern[1]))
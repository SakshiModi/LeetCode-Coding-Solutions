class Solution:
    def lengthOfLastWord(self, s):
        lst=s.strip().split(' ')
        count=len(lst[len(lst)-1])
        return count
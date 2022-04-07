class Solution:
    def longestCommonPrefix(self, strs):
        flag=strs[0]
        for i in strs:
            if(len(i)<len(flag)):
                flag=i
        count=len(strs)-1
        while(count>=0):
            if strs[count].startswith(flag):
                count=count-1
            else:
                flag=flag[0:len(flag)-1]
                count=len(strs)-1
        return flag
            
        
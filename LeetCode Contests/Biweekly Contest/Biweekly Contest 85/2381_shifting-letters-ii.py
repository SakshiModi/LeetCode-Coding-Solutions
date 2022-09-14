class Solution:
    def shiftingLetters(self, s, shifts):
        lst=[0]*len(s)
        for i,j,k in shifts:
            if k==0:
                flag=-1
            else:
                flag=+1
            lst[i]+=flag
            if j<len(s)-1:
                lst[j+1]-=flag
        n=len(lst)
        for i in range(1,n):
            lst[i]+=lst[i-1]
        ans=""
        for ind in range(len(s)):
            lst[ind]=lst[ind]%26
            temp=(ord(s[ind])+lst[ind])
            if temp>122:
                temp=temp-26
            ans+=chr(temp)
        return ans
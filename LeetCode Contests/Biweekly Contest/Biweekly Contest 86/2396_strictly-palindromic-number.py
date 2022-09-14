class Solution:
    def isPalindrome(self,val):
        if val==val[::-1]:
            return True
        return False
    def pal_func(self,num,flag):
        idx=1
        while(idx<num):
            idx=idx*flag
        if idx!=num:
            idx=idx//flag
        ans=""
        while(idx>0):
            ans=ans+str(num//idx)
            num=num%idx
            idx=idx//flag
        return self.isPalindrome(ans)
    def isStrictlyPalindromic(self, n: int) -> bool:
        for idx in range(2,n-1):
            if not self.pal_func(n,idx):
                return False
        return True
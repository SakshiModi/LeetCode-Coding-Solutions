class Solution:
    def isPalindrome(self, x):
        if(x>=0):
            n=x
            ans=0
            while(n>0):
                r=n%10
                n=n//10
                ans=(ans*10)+r
            if(ans==x):
                return True
            else:
                return False
        else:
            return False
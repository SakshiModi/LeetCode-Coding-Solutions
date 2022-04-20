class Solution:
    def powOfNumbers(self,x,n):
        if n==0:
            return 1
        elif n==1:
            return x
        elif n%2==0:
            if(n>0):
                return self.powOfNumbers(x*x,n//2)
            else:
                n=0-n
                return 1/self.powOfNumbers(x*x,n//2)
        else:
            if(n>0):
                return x*self.powOfNumbers(x*x,n//2)
            else:
                n=0-n
                return 1/(x*self.powOfNumbers(x*x,n//2))
    def myPow(self, x, n):
        ans=self.powOfNumbers(x,n)
        return ans

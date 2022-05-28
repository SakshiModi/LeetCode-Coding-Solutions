class Solution:
    def gcd(self,n1,n2):
        if (n1<n2):
            self.gcd(n2,n1)
        if n2==0:
            return n1
        return self.gcd(n2,n1%n2)
    def minimumLines(self, stockPrices):
        stockPrices=sorted(stockPrices)
        ans=[]
        for i in range(1,len(stockPrices)):
            n1=stockPrices[i][1]-stockPrices[i-1][1]
            n2=stockPrices[i][0]-stockPrices[i-1][0]
            gcd_num=self.gcd(abs(n1),abs(n2))
            temp=(n1//gcd_num,n2//gcd_num)
            if len(ans)!=0:
                if ans[-1]!=temp:
                    ans.append(temp)
            else:
                ans.append(temp)
        return len(ans)
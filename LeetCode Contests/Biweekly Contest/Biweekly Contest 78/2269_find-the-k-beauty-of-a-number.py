class Solution:
    def divisorSubstrings(self, num, k):
        i=0
        number=str(num)
        n=len(number)
        ans=0
        while(i<n-k+1):
            temp=int(number[i:i+k])
            if temp!=0:
                if num%temp==0:
                    ans+=1
            i+=1
        return ans
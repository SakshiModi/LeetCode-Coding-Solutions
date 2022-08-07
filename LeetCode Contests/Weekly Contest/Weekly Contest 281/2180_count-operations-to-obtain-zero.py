class Solution:
    def countEven(self, num):
        count=0
        for i in range(1,num+1):
            n=i
            sumNow=0
            while(n>0):
                rem=n%10
                sumNow+=rem
                n=n//10
            if sumNow<=num and sumNow%2==0:
                count+=1
        return count
        
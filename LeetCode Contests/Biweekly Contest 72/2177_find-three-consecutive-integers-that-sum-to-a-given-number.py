class Solution:
    def sumOfThree(self, num):
        a=num//3
        rem=num%3
        if rem==0:
            return [a-1,a,a+1]
        else:
            return []
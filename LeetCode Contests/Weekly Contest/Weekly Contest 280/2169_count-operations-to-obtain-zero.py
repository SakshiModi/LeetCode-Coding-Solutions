class Solution:
    def countOperations(self, num1, num2):
        count=0
        while(num1!=0 and num2!=0):
            if num1<num2:
                num1,num2=num2,num1
            sub=num1-num2
            num1=sub
            count+=1
        return count
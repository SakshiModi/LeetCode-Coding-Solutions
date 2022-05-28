class Solution:
    def removeDigit(self, number, digit):
        lst=[]
        for i in range(len(number)):
            if number[i]==digit:
                lst.append(int(number[:i]+number[i+1:]))
        return str(max(lst))
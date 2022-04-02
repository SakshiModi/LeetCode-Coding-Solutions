class Solution:
    def romanToInt(self, s):
        dict={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        n=len(s)
        sum=dict[s[0]]
        for i in range(1,n):
            if((s[i]=='V' or s[i]=='X') and s[i-1]=='I'):
                sum=sum+dict[s[i]]-(2*dict['I'])
            elif((s[i]=='L' or s[i]=='C') and s[i-1]=='X'):
                sum=sum+dict[s[i]]-(2*dict['X'])
            elif((s[i]=='D' or s[i]=='M') and s[i-1]=='C'):
                sum=sum+dict[s[i]]-(2*dict['C'])
            else:
                sum=sum+dict[s[i]]
        return sum
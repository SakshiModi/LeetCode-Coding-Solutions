class Solution:
    def longestValidParentheses(self, s):
        n=len(s)
        lst=[['',0]]
        ans=0
        for i in range(n):
            if(s[i]=='('):
                lst.append(['(',0])
            elif(s[i]==')'):
                if(lst[-1][0]=='('):
                    count=lst[-1][1]+2
                    lst.pop(-1)
                    lst[-1][1]+=count
                else:
                    lst.append([')',0])
        for i in lst:
            if(i[1]>ans):
                ans=i[1]
        return ans
class Solution:
    def generateParenthesis(self, n):
        ans=['()']
        if n==1:
            return ans
        x=1
        while(x<n):
            lst=set()
            for i in ans:
                for j in range(len(i)):
                    lst.add(i[:j]+"()"+i[j:])
            x+=1
            ans=list(lst)
        return ans
class Solution:
    def minimumSum(self, num):
        lst=sorted(list(str(num)))
        n=len(lst)
        temp=[]
        for i in range(n//2):
            temp.append(lst[i]+lst[n-1-i])
            ans=0
        for i in temp:
            ans+=int(i)
        return ans
        
class Solution:
    def findWinners(self, matches):
        a=set()
        b=set()
        d={}
        for i,j in matches:
            a.add(i)
            b.add(j)
            if j in d:
                d[j]+=1
            else:
                d[j]=1
        ans=[]
        for k,v in d.items():
            if v==1:
                ans.append(k)
        ans2=sorted(list(a-b))
        ans=sorted(ans)
        return [ans2,ans]
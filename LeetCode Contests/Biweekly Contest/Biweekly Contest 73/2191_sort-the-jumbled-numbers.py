class Solution:
    def sortJumbled(self, mapping, nums):
        n=len(mapping)
        mainDict={}
        for i in range(n):
            mainDict[i]=mapping[i]
        ans={}
        for i in nums:
            temp=i
            sumNow=""
            if temp==0:
                sumNow=str(mainDict[0])
            while(temp>0):
                rem=temp%10
                sumNow=str(mainDict[rem])+sumNow
                temp=temp//10
            temp2=int(sumNow)
            if temp2 not in ans:
                ans[temp2]=[i]
            else:
                ans[temp2].append(i)
        res=[]
        keys=list(ans.keys())
        for k in sorted(keys):
            res.extend(ans[k])
        return res
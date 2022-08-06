class Solution:
    def possibleTime(self,seconds):
        ans=[]
        minute=seconds//60
        leftSeconds=seconds%60
        if minute<100:
            if leftSeconds<10:
                ans.append(int(str(minute)+"0"+str(leftSeconds)))
            else:
                ans.append(int(str(minute)+str(leftSeconds)))
            if minute>1 and leftSeconds+60<100:
                ans.append(int(str(minute-1)+str(leftSeconds+60)))
        else:
            ans.append(int(str(minute-1)+str(leftSeconds+60)))
        if seconds<100:
            ans.append(seconds)
        return ans
            
    def minCostSetTime(self, startAt, moveCost, pushCost, targetSeconds):
        temp=self.possibleTime(targetSeconds)
        ans=inf
        for i in temp:
            time=str(i)
            n=len(time)
            flag=0
            newStartAt=str(startAt)
            print(time)
            for j in range(n):
                if newStartAt==time[j]:
                    flag+=pushCost
                else:
                    flag+=pushCost+moveCost
                    newStartAt=time[j]
            ans=min(ans,flag)
            print(flag)
        return ans
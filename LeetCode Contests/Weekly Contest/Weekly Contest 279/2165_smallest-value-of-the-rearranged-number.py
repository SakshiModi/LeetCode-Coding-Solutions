class Solution:
    def smallestNumber(self, num):
        numStr=str(num)
        if num==0:
            return 0
        if numStr[0]=="-":
            lst=list(numStr[1:])
            lst=sorted(lst,reverse=True)
            ans=""
            for i in lst:
                ans+=i
            return (0-int(ans))
        else:
            lst=list(numStr)
            lst=sorted(lst)
            exchange=1
            while(lst[0]=="0"):
                lst[0],lst[exchange]=lst[exchange],lst[0]
                exchange+=1
            ans=""
            for i in lst:
                ans+=i
            return int(ans)
            
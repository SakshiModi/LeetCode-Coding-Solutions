class Solution:
    def maximumEvenSplit(self, finalSum):
        if finalSum%2==1:
            return []
        div=finalSum//2
        sumNow=2
        lst=[2]
        while(sumNow<finalSum):
            lst.append(lst[-1]+2)
            sumNow+=lst[-1]
        if sumNow>finalSum or len(set(lst))!=len(lst):
            temp=lst.pop(-1)
            lst[-1]+=temp-sumNow+finalSum
        return lst
class Solution:
    def taskSchedulerII(self, tasks, space):
        daynow=0
        prevdaydict={}
        for task in tasks:
            if task not in prevdaydict :
                daynow+=1
            elif daynow-prevdaydict[task]>=space:
                daynow+=1
            else:
                daynow=prevdaydict[task]+space+1
            prevdaydict[task]=daynow
        return daynow
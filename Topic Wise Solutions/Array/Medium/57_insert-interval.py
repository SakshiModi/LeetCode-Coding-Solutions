class Solution:
    def insert(self, intervals, newInterval):
        count=1
        i=0
        if len(intervals)==0:
            intervals.insert(0,newInterval)
            return intervals
        while(i<len(intervals)):
            if newInterval[0]==intervals[i][0]:
                intervals[i][1]=max(newInterval[1],intervals[i][1])
                i=len(intervals)
            elif i==0 and newInterval[0]<intervals[0][0]:
                intervals.insert(0,newInterval)
                i=len(intervals)
            elif i==len(intervals)-1 and newInterval[0]>intervals[i][0]:
                intervals.insert(len(intervals),newInterval)
                i=len(intervals)
            elif newInterval[0]<intervals[i][0] and newInterval[0]>intervals[i-1][0]:
                intervals.insert(i,newInterval)
                i=len(intervals)
            else:
                i+=1     
        i=0
        while(i<len(intervals)-1):
            if(intervals[i][1]>=intervals[i+1][0]):
                intervals[i][1]=max(intervals[i][1],intervals[i+1][1])
                intervals.pop(i+1)
                i=i-1
            i+=1       
        return intervals
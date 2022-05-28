class Solution:
    def maximumCandies(self, candies, k):
        sumAll=sum(candies)
        if k>sumAll:
            return 0
        time=2
        end=0
        sub=1
        while(time!=end+1):
            sub=1
            time=end+1
            while(True):
                count=0
                for i in candies:
                    count+=i//time
                if count<k:
                    break
                end=time
                sub*=2
                time+=sub
        return time-1
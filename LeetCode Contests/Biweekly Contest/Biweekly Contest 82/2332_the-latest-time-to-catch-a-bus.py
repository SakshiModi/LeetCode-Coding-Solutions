from heapq import heapify,heappush,heappop
class Solution:
    def latestTimeCatchTheBus(self, buses, passengers, capacity):
        buses=sorted(buses)
        end=buses[-1]
        end_time=buses[-1]
        all_pass=set(passengers)
        heapify(passengers)
        while(buses):
            bus_now=buses.pop(0)
            count_now=0
            while(passengers and passengers[0]<=bus_now and count_now<capacity):
                end=heappop(passengers)
                count_now+=1
        if count_now==capacity:
            pass
        else:
            end=end_time
        while(True):
                if end not in all_pass:
                    return end
                end-=1
class Solution:
    def maximumBags(self, capacity, rocks, additionalRocks):
        n=len(capacity)
        count=0
        req_set=[]
        for i in range(n):
            req_set.append(capacity[i]-rocks[i])
        req_set.sort()
        for i in req_set:
            if additionalRocks>=i:
                count+=1
                additionalRocks-=i
            else:
                break
        return count
            
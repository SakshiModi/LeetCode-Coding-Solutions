class Solution:
    def minimumCardPickup(self, cards):
        pos={}
        for i in range(len(cards)):
            if cards[i] in pos:
                pos[cards[i]].append(i)
            else:
                pos[cards[i]]=[i]
        minval=inf
        count=0
        for k,v in pos.items():
            if len(v)>1:
                for i in range(len(v)-1):
                    temp=v[i+1]-v[i]+1
                    if temp<minval:
                        minval=temp
                count=1
        if count==0:
            return -1
        else:
            return minval
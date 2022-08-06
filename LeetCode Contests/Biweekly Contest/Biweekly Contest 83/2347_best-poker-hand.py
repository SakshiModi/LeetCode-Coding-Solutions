class Solution:
    def bestHand(self, ranks, suits):
        freq={}
        high=0
        ranks_set=set(ranks)
        n=len(set(suits))
        if n==1:
            return "Flush"
        for i in ranks:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
            high=max(high,freq[i])
        if high>=3:
            return "Three of a Kind"
        if high==2:
            return "Pair"
        return "High Card"
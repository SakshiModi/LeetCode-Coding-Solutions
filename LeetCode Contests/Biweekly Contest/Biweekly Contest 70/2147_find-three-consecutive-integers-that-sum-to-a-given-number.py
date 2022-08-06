class Solution:
    def numberOfWays(self, corridor):
        while(len(corridor)>0 and corridor[0]=='P'):
            corridor=corridor[1:]
        while(len(corridor)>0 and corridor[-1]=='P'):
            corridor=corridor[:-1]
        n=len(corridor)
        count=0
        freq=[]
        i=0
        while(i<n):
            freqOfP=0
            while i<n and count%2==0 and corridor[i]=='P':
                freqOfP+=1
                i+=1
            if count%2==0:
                freq.append(freqOfP)
            if i<n and corridor[i]=='S':
                count+=1
                i+=1
            else:
                i+=1
        if count%2==1:
            return 0
        elif count==0:
            return 0
        else:
            prod=1
            i=0
            m=len(freq)
            while(i<m):
                prod*=(freq[i]+1)
                i+=1
            return prod%((10**9)+7)
        
            
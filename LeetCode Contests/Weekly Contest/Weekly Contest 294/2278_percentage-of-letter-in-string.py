class Solution:
    def percentageLetter(self, s, letter):
        freq={}
        total=0
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
            total+=1
        if letter in freq:
            return freq[letter]*100//total
        else:
            return 0
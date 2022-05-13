class Solution:
    def plusOne(self, digits):
        revDig=digits[::-1]
        i=0
        while(i<len(digits)):
            newSum=revDig[i]+1
            if newSum>9:
                revDig[i]=newSum%10
                i+=1
                if(i==len(revDig)):
                    revDig.append(1)
                    break
            else:
                revDig[i]=newSum
                break
        return revDig[::-1]
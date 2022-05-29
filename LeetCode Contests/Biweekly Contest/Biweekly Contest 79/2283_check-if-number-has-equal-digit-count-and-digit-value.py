class Solution:
    def digitCount(self, num):
        freq={}
        for i in num:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        for i in range(len(num)):
            if str(i) not in freq:
                if int(num[i])!=0:
                    return False
            elif freq[str(i)]!=int(num[i]):
                #print(i,freq[num[i]])
                return False
        return True
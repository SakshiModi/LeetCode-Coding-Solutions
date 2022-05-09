class Solution:
    def largestGoodInteger(self, num):
        n=len(num)
        i=0
        ans=""
        while(i<n-2):
            if num[i]==num[i+1] and num[i]==num[i+2]:
                if ans=="":
                    ans=num[i:i+3]
                elif int(ans)<int(num[i:i+3]):
                    ans=num[i:i+3]
            i+=1
        return ans
            
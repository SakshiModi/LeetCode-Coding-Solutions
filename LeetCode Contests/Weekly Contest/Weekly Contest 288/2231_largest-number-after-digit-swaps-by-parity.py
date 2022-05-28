class Solution:
    def largestInteger(self, num):
        num=str(num)
        odd_pos=set()
        odd=[]
        even=[]
        for i in range(len(num)):
            if int(num[i])%2==0:
                even.append(num[i])
            else:
                odd.append(num[i])
                odd_pos.add(i)
        even=sorted(even,reverse=True)
        odd=sorted(odd,reverse=True)
        x=0
        y=0
        ans=""
        for i in range(len(num)):
            if i in odd_pos:
                ans+=odd[x]
                x+=1
            else:
                ans+=even[y]
                y+=1
        return int(ans)
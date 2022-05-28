class Solution:
    def countTexts(self, pressedKeys):
        dig3={0:1,1:1,2:2,3:4}
        dig4={0:1,1:1,2:2,3:4,4:8}
        n=len(pressedKeys)
        i=0
        stack=[]
        while(i<n):
            if len(stack)==0:
                stack.append([pressedKeys[i],1])
            else:
                if stack[-1][0]==pressedKeys[i]:
                    stack[-1][1]+=1
                else:
                    stack.append([pressedKeys[i],1])
            i+=1
        #print(stack)
        ans=1
        for i,j in stack:
            if i=='7' or i=='9':
                if j in dig4:
                    ans*=dig4[j]
                else:
                    for k in range(len(dig4),j+1):
                        dig4[k]=dig4[k-1]+dig4[k-2]+dig4[k-3]+dig4[k-4]
                    ans*=dig4[j]
            else:
                if j in dig3:
                    ans*=dig3[j]
                else:
                    for k in range(len(dig3),j+1):
                        dig3[k]=dig3[k-1]+dig3[k-2]+dig3[k-3]
                    ans*=dig3[j]
        return ans%((10**9)+7)
                
class Solution:
    def multiply(self, num1, num2):
        num1=num1[::-1]
        num2=num2[::-1]
        m=len(num1)
        n=len(num2)
        ans=[0 for i in range(m+n)]
        for i in range(m):
            temp1=int(num1[i])
            for j in range(n):
                temp2=int(num2[j])
                mul=temp1*temp2
                rem=mul%10
                div=mul//10
                ans[i+j]+=rem
                ans[i+j+1]+=div
        for i in range(len(ans)):
            if ans[i]>9:
                ans[i+1]+=ans[i]//10
                ans[i]=ans[i]%10
        ans=ans[::-1]
        #print(ans)
        result="".join(map(str,ans))
        flag=len(result)-1
        for i in range(len(result)):
            if result[i]!='0':
                flag=i
                break
        return result[flag:]

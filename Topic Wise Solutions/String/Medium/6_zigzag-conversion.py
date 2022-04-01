class Solution:
    def convert(self, s, numRows):
        n=len(s)
        ans=s
        if(numRows>1):
            ans=''
            elem=(numRows*2)-2
            div=n//elem
            rem=n%elem
            rem2=0
            if(rem!=0):
                rem2=1              
            iterate=div+rem2+1
            for i in range(0,numRows):
                count=0
                for j in range(0,iterate):
                    if(i==0 or i==numRows-1):
                        if((i+(j*elem))<n):
                            ans=ans+s[i+(j*elem)]
                    else:
                        if((i+(j*elem)-(i*2))<n and count==1):
                            ans=ans+s[i+(j*elem)-(i*2)]
                        if((i+(j*elem))<n):
                            ans=ans+s[i+(j*elem)]
                        count=1
        return ans
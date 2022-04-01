class Solution:
    def myAtoi(self, s):
        i=0
        n=len(s)
        if n>0 and s[0] in " 01234567889-+":
            st=""
            flag=0
            while(i<n and s[i]==" "):
                i+=1
            if i<n and (s[i]=="-" or s[i]=="+"):
                flag=s[i]
                i+=1
            while(i<n and s[i] in "0123456789"):
                st+=s[i]
                i+=1
            if len(st)>0:
                x=int(st)
                if flag=="+" and x>=(2**31)-1:
                    return (2**31)-1
                elif flag=="-" and x>=2**31:
                    return 0-(2**31)
                elif x>(2**31)-1:
                    return (2**31)-1
                else:
                    if flag=="-":
                        return 0-x
                    elif flag=="+":
                        return x
                    else:
                        return x
            else:
                return 0
        else:
            return 0
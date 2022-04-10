class Solution:
    def isValid(self, s):
        lst=[]
        ans=True
        for i in range(0,len(s)):
            if(len(lst)==0):
                if(s[i]=='(' or s[i]=='{' or s[i]=='['):
                    lst.append(s[i])
                else:
                    ans=False
                    break
            elif(len(lst)==1):
                if((lst[0]=='(' and s[i]==')') or (lst[0]=='{' and s[i]=='}') or (lst[0]=='[' and s[i]==']')):
                    del lst[0]
                elif(s[i]=='(' or s[i]=='{' or s[i]=='['):
                    lst.append(s[i])
                else:
                    ans=False
                    break
            else:
                if((lst[len(lst)-1]=='(' and s[i]==')') or (lst[len(lst)-1]=='{' and s[i]=='}') or (lst[len(lst)-1]=='[' and s[i]==']')):
                    del lst[len(lst)-1]
                elif(s[i]=='(' or s[i]=='{' or s[i]=='['):
                    lst.append(s[i])
                else:
                    ans=False
                    break   
        if(len(lst)!=0):
            ans=False
        return ans
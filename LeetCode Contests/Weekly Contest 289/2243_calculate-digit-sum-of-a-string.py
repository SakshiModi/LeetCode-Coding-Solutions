class Solution:
    def digitSum(self, s, k):
        while(len(s)>k):
            new_s=""
            for i in range(0,len(s),k):
                temp=0
                if i+k>=len(s):
                    for j in range(i,len(s)):
                        temp+=int(s[j])
                else:
                    for j in range(i,i+k):
                        temp+=int(s[j])
                new_s+=str(temp)
            s=new_s
        return s
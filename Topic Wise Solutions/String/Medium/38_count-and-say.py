class Solution:
    def findString(self,n):
        x=n[0]
        count=0
        st=""
        for i in range(len(n)):
            if(n[i]==x):
                count=count+1
            else:
                st=st+str(count)+x
                x=n[i]
                count=1
        st=st+str(count)+x
        return st
            
    def countAndSay(self, n):
        temp="1"
        for i in range(1,n):
            temp=self.findString(temp)
        return temp
if __name__=="__main__":
	sol=Solution()
	n = 1
	print(sol.countAndSay(n))
	n = 4
	print(sol.countAndSay(n))
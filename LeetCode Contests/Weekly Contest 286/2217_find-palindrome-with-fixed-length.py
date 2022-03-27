class Solution:
    def kthPalindrome(self, queries, intLength):
        start_elem=(10**(intLength//2))
        if intLength%2==0:
            start_elem=start_elem//10
        m=len(str(start_elem))
        rem=intLength-m
        ans=[]
        for i in range(len(queries)):
            temp=str(queries[i]+start_elem-1)
            print(temp)
            if len(temp)==m:
                temp=temp+temp[:rem][::-1]
                ans.append(int(temp))
            else:
                ans.append(-1)
        return ans
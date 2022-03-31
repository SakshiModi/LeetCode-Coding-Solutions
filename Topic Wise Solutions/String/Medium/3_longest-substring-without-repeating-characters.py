class Solution:
    def lengthOfLongestSubstring(self, s):
        n=len(s)
        maxLength=0
        x=0
        y=n
        while(x<y):
            st=s[x]
            for i in range(x+1,n):
                if st.find(s[i])==-1:
                    st+=s[i]
                else:
                    break
            x+=1
            if maxLength<len(st):
                maxLength=len(st)
                y=n-maxLength
        return maxLength
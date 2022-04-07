class Solution:
    def letterCombinations(self, digits):
        dict={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        ans=[]
        for i in digits:
            if(len(ans)==0):
                ans=dict[i]
            else:
                temp=[]
                for j in ans:
                    for k in dict[i]:
                        temp.append(j+k)
                ans=temp
        return ans
            
        
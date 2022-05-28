from functools import lru_cache
class Solution:
    def maxValueOfCoins(self, piles, k):
        n=len(piles)
        main_lst=[]
        for i in range(n):
            temp=[piles[i][0]]
            for j in range(1,min(k,len(piles[i]))):
                temp.append(piles[i][j]+temp[-1])
            main_lst.append(temp)
        #print(main_lst)
        @lru_cache(None)
        def dp(index,rem_k):
            if index==len(main_lst):
                if rem_k==0:
                    return 0
                else:
                    return -inf
            ans=dp(index+1,rem_k)
            for i in range(len(main_lst[index])):
                if i<rem_k:
                    ans=max(ans,main_lst[index][i]+dp(index+1,rem_k-i-1))
            return ans
        return dp(0,k)
        
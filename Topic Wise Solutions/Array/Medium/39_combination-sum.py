class Solution:
    def findSol(self,candidates,target,ans,listNow,ind):
        if target<0:
            return
        if target==0:
            return ans.append(listNow.copy())
        while(ind<len(candidates)):
            listNow.append(candidates[ind])
            self.findSol(candidates,target-candidates[ind],ans,listNow,ind)
            listNow.pop(-1)
            if candidates[ind]>target:
                break
            ind+=1
    def combinationSum(self, candidates, target):
        ans=[]
        self.findSol(sorted(candidates),target,ans,[],0)
        return ans
sol=Solution()
print(sol.combinationSum(candidates = [2,3,6,7], target = 7))
print(sol.combinationSum(candidates = [2,3,5], target = 8))
print(sol.combinationSum([2],1))
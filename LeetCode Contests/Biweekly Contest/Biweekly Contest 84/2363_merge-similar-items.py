class Solution:
    def mergeSimilarItems(self, items1, items2):
        maindict={}
        for i,j in items1:
            if i not in maindict:
                maindict[i]=0
            maindict[i]+=j
        for i,j in items2:
            if i not in maindict:
                maindict[i]=0
            maindict[i]+=j
        ans=[]
        keys=sorted(list(maindict.keys()))
        for i in keys:
            ans.append([i,maindict[i]])
        return ans
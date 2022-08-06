class Solution:
    def successfulPairs(self, spells, potions, success):
        potions=sorted(potions)
        n=len(potions)
        list_now=[]
        for idx,elem in enumerate(spells):
            list_now.append([elem,idx])
        list_now=sorted(list_now)
        main_dict={}
        for elem,idx in list_now:
            while(n>0 and elem*potions[n-1]>=success):
                n-=1
            main_dict[idx]=len(potions)-n
        ans=[]
        m=len(spells)
        for i in range(m):
            ans.append(main_dict[i])
        return ans
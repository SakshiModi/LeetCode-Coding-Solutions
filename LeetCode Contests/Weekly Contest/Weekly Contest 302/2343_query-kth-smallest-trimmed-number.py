class Solution:
    def smallestTrimmedNumbers(self, nums, queries):
        ans=[]
        for x,y in queries:
            lst=[]
            for n in nums:
                lst.append(int(n[len(n)-y:]))
            pos={}
            for ind,elem in enumerate(lst):
                if elem not in pos:
                    pos[elem]=[ind]
                else:
                    pos[elem].append(ind)
            lst=sorted(lst)
            x-=1
            elem_now=lst[x]
            pos_now=0
            while(x>0 and lst[x]==lst[x-1]):
                pos_now+=1
                x-=1
            ans.append(pos[elem_now][pos_now])
        return ans
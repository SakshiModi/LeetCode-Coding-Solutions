from collections import deque
class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        main_dict={}
        m=len(mat)
        n=len(mat[0])
        for i in range(m):
            main_dict[i]=set()
            for j in range(n):
                if mat[i][j]==1:
                    main_dict[i].add(j)
        col=[]
        for i in range(n):
            col.append(i)
        self.temp_lst=[]
        def internal(count,int_set):
            if len(int_set)==cols:
                self.temp_lst.append(int_set.copy())
                return
            if count==len(mat[0]):
                return 
            internal(count+1,int_set)
            int_set.add(col[count])
            internal(count+1,int_set)
            int_set.remove(col[count])
        internal(0,set())
        ans=0
        for i in self.temp_lst:
            count=0
            for j,value in main_dict.items():
                if value.issubset(i):
                    count+=1
            ans=max(ans,count)
        return ans
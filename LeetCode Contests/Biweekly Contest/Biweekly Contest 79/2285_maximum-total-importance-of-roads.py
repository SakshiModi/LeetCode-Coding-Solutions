class Solution:
    def maximumImportance(self, n, roads):
        edge_count={}
        result=0
        for i in range(n):
            edge_count[i]=0
        for start,end in roads:
            edge_count[start]+=1
            edge_count[end]+=1
        all_counts=sorted(list(edge_count.values()))
        m=len(all_counts)
        for i in range(m):
            temp=(i+1)*all_counts[i]
            result+=temp
        return result
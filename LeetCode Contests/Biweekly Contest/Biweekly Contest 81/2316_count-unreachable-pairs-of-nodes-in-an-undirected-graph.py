class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]
    def dfs(self, temp, v, visit):
        visit[v] = True
        temp.append(v)
        for i in self.adj[v]:
            if visit[i] == False:
                temp = self.dfs(temp, i, visit)
        return temp
    def adding_edge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
    def components(self):
        visit = []
        cc = []
        for i in range(self.V):
            visit.append(False)
        for v in range(self.V):
            if visit[v] == False:
                temp = []
                cc.append(self.dfs(temp, v, visit))
        return cc
class Solution:
    def countPairs(self, n: int, edges):
        gr=Graph(n)
        for i,j in edges:
            gr.adding_edge(i,j)
        lst=gr.components()
        ans=0
        for i in lst:
            ans+=(len(i)*(len(i)-1))//2
        return (n*(n-1))//2-ans
            
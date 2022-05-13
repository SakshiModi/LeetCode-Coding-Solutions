class Solution:
    def uniquePaths(self, m, n):
        grid=[]
        for i in range(m):
            temp=[]
            for j in range(n):
                if i==0 or j==0:
                    temp.append(1)
                else:
                    temp.append(0)
            grid.append(temp)
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j]+=grid[i-1][j]+grid[i][j-1]
        return grid[m-1][n-1]
        
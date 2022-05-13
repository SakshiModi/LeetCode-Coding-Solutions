class Solution:
    def minPathSum(self, grid):
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if i==0 and j>0:
                    grid[i][j]+=grid[i][j-1]
                elif j==0 and i>0:
                    grid[i][j]+=grid[i-1][j]
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j]+=min(grid[i][j-1],grid[i-1][j])
        return grid[m-1][n-1]
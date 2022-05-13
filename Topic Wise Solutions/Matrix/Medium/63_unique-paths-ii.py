class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        rows=0
        cols=0
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    obstacleGrid[i][j]="obs"
                    if i==0:
                        rows=1
                    if j==0:
                        cols=1
                elif i==0 and rows==0:
                    obstacleGrid[i][j]=1
                elif j==0 and cols==0:
                    obstacleGrid[i][j]=1
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]!='obs':
                    if obstacleGrid[i-1][j]!='obs':
                        obstacleGrid[i][j]+=obstacleGrid[i-1][j]
                    if obstacleGrid[i][j-1]!='obs':
                        obstacleGrid[i][j]+=obstacleGrid[i][j-1]
        if obstacleGrid[m-1][n-1]=="obs":
            return 0
        return obstacleGrid[m-1][n-1]
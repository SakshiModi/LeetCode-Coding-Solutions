class Solution:
    def countUnguarded(self, m, n, guards, walls):
        mat=[]
        for i in range(m):
            temp=[]
            for j in range(n):
                temp.append('empty')
            mat.append(temp)
        for i,j in guards:
            mat[i][j]='guard'
        for i,j in walls:
            mat[i][j]='wall'
        used=set()
        for i,j in guards:
            x=i
            while x-1>=0:
                if mat[x-1][j]=='empty':
                    used.add((x-1,j))
                    x-=1
                else:
                    break
            x=i
            while x+1<m:
                if mat[x+1][j]=='empty':
                    used.add((x+1,j))
                    x+=1
                else:
                    break
            y=j
            while y-1>=0:
                if mat[i][y-1]=='empty':
                    used.add((i,y-1))
                    y-=1
                else:
                    break
            y=j
            while y+1<n:
                if mat[i][y+1]=='empty':
                    used.add((i,y+1))
                    y+=1
                else:
                    break
        print(used)
        return (m*n)-len(guards)-len(walls)-len(used)
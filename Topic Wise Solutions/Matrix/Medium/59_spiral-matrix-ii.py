class Solution:
    def generateMatrix(self, n):
        start=0
        end_x=n
        end_y=n
        count=0
        n1=end_x//2
        elemCount=0
        totalElem=n*n
        pushElem=1
        matrix=[]
        for i in range(n):
            x=[]
            for j in range(n):
                x.append(0)
            matrix.append(x)
        while(count<n1+1):
            for i in range(start,end_y):
                matrix[start][i]=pushElem
                pushElem+=1
                elemCount+=1
            if elemCount==totalElem:
                break
            for i in range(start+1,end_x):
                matrix[i][end_y-1]=pushElem
                pushElem+=1
                elemCount+=1
            if elemCount==totalElem:
                break
            for i in range(end_y-2,start-1,-1):
                matrix[end_x-1][i]=pushElem
                pushElem+=1
                elemCount+=1
            if elemCount==totalElem:
                break
            for i in range(end_x-2,start,-1):
                matrix[i][start]=pushElem
                pushElem+=1
                elemCount+=1
            count+=1
            start+=1
            end_x-=1
            end_y-=1
        return matrix
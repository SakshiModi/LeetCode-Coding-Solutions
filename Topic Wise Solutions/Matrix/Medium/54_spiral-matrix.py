class Solution:
    def spiralOrder(self, matrix):
        ans=[]
        start=0
        end_x=len(matrix)
        end_y=len(matrix[0])
        count=0
        n1=end_x//2
        elemCount=0
        totalElem=end_x*end_y
        while(count<n1+1):
            for i in range(start,end_y):
                ans.append(matrix[start][i])
                elemCount+=1
            if elemCount==totalElem:
                break
            for i in range(start+1,end_x):
                ans.append(matrix[i][end_y-1])
                elemCount+=1
            if elemCount==totalElem:
                break
            for i in range(end_y-2,start-1,-1):
                ans.append(matrix[end_x-1][i])
                elemCount+=1
            if elemCount==totalElem:
                break
            for i in range(end_x-2,start,-1):
                ans.append(matrix[i][start])
                elemCount+=1
            count+=1
            start+=1
            end_x-=1
            end_y-=1
        return ans
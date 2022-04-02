class Solution:
    def intToRoman(self, num):
        ans=""
        lst=[]
        valLst=[['I','V'],['X','L'],['C','D'],['M','']]
        n=num
        while(n>0):
            lst.append(n%10)
            n=n//10
        for x,y in enumerate(lst):
            if y==0:
                ans=""+ans
            elif y<4:
                ans=(valLst[x][0]*y)+ans
            elif y==4:
                ans=valLst[x][0]+valLst[x][1]+ans
            elif y==5:
                ans=valLst[x][1]+ans
            elif y<9:
                ans=valLst[x][1]+(valLst[x][0]*(y-5))+ans
            elif y==9:
                ans=valLst[x][0]+valLst[x+1][0]+ans
        return ans
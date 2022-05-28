class Solution:
    def maximumWhiteTiles(self, tiles, carpetLen):
        tiles=sorted(tiles,key=lambda x:x[0])
        n=len(tiles)
        tiles2=[tiles[0]]
        length_temp=tiles[0][1]-tiles[0][0]+1
        if length_temp>=carpetLen:
            return carpetLen
        for i in range(1,n):
            if tiles2[-1][1]+1==tiles[i][0]:
                tiles2[-1][1]=tiles[i][1]
            else:
                tiles2.append(tiles[i])
            length_temp=tiles2[-1][1]-tiles2[-1][0]+1
            if length_temp>=carpetLen:
                return carpetLen
        ans=0
        ptr1=0
        ptr2=0
        total_sum=0
        total_tiles=0
        while(ptr1<len(tiles2)):
            while(ptr2<len(tiles2) and tiles2[ptr2][1]-tiles2[ptr1][0]<carpetLen-1):
                total_tiles+=tiles2[ptr2][1]-tiles2[ptr2][0]+1
                ptr2+=1
            if ptr2==len(tiles2):
                ans=max(ans,total_tiles)
                break
            if tiles2[ptr2][0]-tiles2[ptr1][0]>carpetLen-1:
                ptr2-=1
                total_tiles-=tiles2[ptr2][1]-tiles2[ptr2][0]+1
            temp=min(carpetLen+tiles2[ptr1][0]-1,tiles2[ptr2][1])
            ans=max(temp-tiles2[ptr2][0]+1+total_tiles,ans)
            total_tiles-=tiles2[ptr1][1]-tiles2[ptr1][0]+1
            ptr1+=1
        return ans
class Solution:
    def maxArea(self, height):
        n=len(height)
        contStart=0
        contEnd=n-1
        maxarea=min(height[contStart],height[contEnd])*(n-1)
        while(contStart<contEnd):
            if(height[contStart]<=height[contEnd]):
                contStart=contStart+1
            elif(height[contStart]>height[contEnd]):
                contEnd=contEnd-1
            area=min(height[contStart],height[contEnd])*(contEnd-contStart)
            if(maxarea<area):
                maxarea=area
        return maxarea
        
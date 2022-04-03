class Solution:
    def convertTime(self, current, correct):
        cur_h=int(current[0:2])
        cur_m=int(current[3:5])
        cor_h=int(correct[0:2])
        cor_m=int(correct[3:5])
        rem=((cor_h*60)+cor_m)-((cur_h*60)+cur_m)
        ans=rem//60
        rem=rem%60
        ans+=rem//15
        rem=rem%15
        ans+=rem//5
        rem=rem%5
        ans+=rem
        return ans
        
            
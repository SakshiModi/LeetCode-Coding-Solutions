class Solution:
    def countLatticePoints(self, circles):
        ans = set()
        for i in circles:
            r = i[2]
            cx, cy = i[0], i[1]
            for x in range(-r,r+1):
                for y in range(-r, r+1):
                    if x*x + y*y <= r* r:
                        ans.add((cx + x, cy + y))
        return len(ans)
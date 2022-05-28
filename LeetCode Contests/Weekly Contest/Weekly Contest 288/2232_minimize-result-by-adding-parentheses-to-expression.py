import math
class Solution:
    def solve_exp(self,expression):
        x,y=expression.split('(')
        z,y=y.split(')')
        if x=="":
            x=1
        else:
            x=int(x)
        if y=="":
            y=1
        else:
            y=int(y)
        exp1,exp2=list(map(int,z.split("+")))
        return (exp1+exp2)*x*y
    def minimizeResult(self, expression):
        part1,part2=expression.split('+')
        minimum=math.inf
        ans=""
        for i in range(len(part1)):
            part1_1=part1[:i]+'('+part1[i:]
            for j in range(1,len(part2)+1):
                part2_1=part2[:j]+')'
                if j<len(part2):
                    part2_1+=part2[j:]
                temp='+'.join([part1_1,part2_1])
                solu=self.solve_exp(temp)
                if solu<minimum:
                    minimum=solu
                    ans=temp
            
        return ans
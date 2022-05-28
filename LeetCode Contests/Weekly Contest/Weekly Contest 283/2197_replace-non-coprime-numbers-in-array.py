from collections import deque
class Solution:
    def gcd(self,a,b):
        if(a<b):
            self.gcd(b,a)
        if b==0:
            return a
        return self.gcd(b,a%b)
    def lcm(self,a,b):
        return (a*b)//self.gcd(a,b)
    def replaceNonCoprimes(self, nums):
        n=len(nums)
        if n<2:
            return nums
        stack=[nums[0]]
        deque_stack=deque(stack)
        i=1
        while(i<n):
            curr_elem=nums[i]
            while(deque_stack):
                num_gcd=self.gcd(deque_stack[-1],curr_elem)
                if num_gcd!=1:
                    elem=deque_stack.pop()
                    curr_elem=(elem*curr_elem)//num_gcd
                else:
                    break
            deque_stack.append(curr_elem)
            i+=1
        return list(deque_stack)
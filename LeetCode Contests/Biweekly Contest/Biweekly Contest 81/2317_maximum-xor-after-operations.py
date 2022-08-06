class Solution:
    def maximumXOR(self, nums):
        set_now=set()
        n=len(nums)
        for i in range(n):
            string_now=bin(nums[i]).replace("0b","")
            temp=0
            for j in string_now[::-1]:
                if j=="1":
                    set_now.add(2**temp)
                temp+=1
        return sum(set_now)
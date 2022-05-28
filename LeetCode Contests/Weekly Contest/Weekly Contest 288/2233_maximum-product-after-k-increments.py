import heapq
class Solution:
    def maximumProduct(self, nums, k):
        freq={}
        n=len(nums)
        for i in range(n):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        keys=list(freq.keys())
        heapq.heapify(keys)
        while(k>0):
            flag=heapq.heappop(keys)
            temp=freq[flag]
            if temp<=k:
                k-=temp
                freq.pop(flag)
                if flag+1 in freq:
                    freq[flag+1]+=temp
                else:
                    freq[flag+1]=temp
                    heapq.heappush(keys,flag+1)
            else:
                freq[flag]=temp-k
                heapq.heappush(keys,flag)
                if flag+1 in freq:
                    freq[flag+1]+=k
                else:
                    freq[flag+1]=k
                    heapq.heappush(keys,flag+1)
                k=0
        ans=1
        for key,val in freq.items():
            ans=ans*(key**val)
        return ans%((10**9)+7)
                
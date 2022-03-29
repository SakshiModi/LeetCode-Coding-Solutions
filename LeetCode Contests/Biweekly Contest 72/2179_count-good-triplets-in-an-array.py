from sortedcontainers import SortedSet
class Solution:
    def goodTriplets(self, nums1, nums2):
        n=len(nums1)
        mainDict={}
        for i in range(n):
            mainDict[nums1[i]]=i
        lst=[]
        freqDict={}
        for i in range(n):
            lst.append(mainDict[nums2[i]])
            freqDict[mainDict[nums2[i]]]=i
        print(freqDict)
        tempSet=SortedSet()
        result=0
        for i in range(n):
            tempSet.add(lst[i])
            ind=tempSet.index(lst[i])
            result+=(ind)*(n-1-freqDict[lst[i]]-lst[i]+ind)#here we are multiplying prefix with suffice
        return result
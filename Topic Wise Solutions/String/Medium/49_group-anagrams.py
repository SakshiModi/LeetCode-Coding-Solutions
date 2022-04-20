class Solution:
    def groupAnagrams(self, strs):
        dict={}
        for i in strs:
            sortStr="".join(sorted(i))
            if sortStr in dict.keys():
                dict[sortStr].append(i)
            else:
                dict.update({sortStr:[i]})
        ans=[]
        for i in dict.keys():
            ans.append(dict[i])
        return ans

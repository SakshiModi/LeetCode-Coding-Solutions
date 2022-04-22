class Solution:
    def merge(self, intervals):
        intervalDict={}
        ans=[]
        intervalKey=set()
        for i in intervals:
            if i[0] not in intervalDict:
                intervalDict.update({i[0]:i[1]})
            else:
                intervalDict[i[0]]=max(intervalDict[i[0]],i[1])
            intervalKey.add(i[0])
        intervalKey=sorted(list(intervalKey))
        for i in range(len(intervalKey)):
            for j in range(i+1,len(intervalKey)):
                if intervalKey[i] in intervalDict.keys():
                    if intervalDict[intervalKey[i]]>=intervalKey[j]:
                        intervalDict[intervalKey[i]]=max(intervalDict[intervalKey[i]],intervalDict[intervalKey[j]])
                        intervalDict.pop(intervalKey[j])
            if intervalKey[i] in intervalDict.keys():
                ans.append([intervalKey[i],intervalDict[intervalKey[i]]])
        return ans

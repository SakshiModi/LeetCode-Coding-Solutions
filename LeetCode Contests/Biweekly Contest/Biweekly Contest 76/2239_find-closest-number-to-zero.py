class Solution:
    def findClosestNumber(self, nums):
        main_dict={}
        for i in nums:
            if i>0:
                if i not in main_dict:
                    main_dict[i]=[i]
                else:
                    main_dict[i].append(i)
            else:
                if 0-i not in main_dict:
                    main_dict[0-i]=[i]
                else:
                    main_dict[0-i].append(i)
        keys=sorted(list(main_dict.keys()))
        return sorted(main_dict[keys[0]],reverse=True)[0] 
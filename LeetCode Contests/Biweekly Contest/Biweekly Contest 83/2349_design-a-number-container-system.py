from sortedcontainers import SortedSet
class NumberContainers:

    def __init__(self):
        self.dict1={}
        self.dict2={}

    def change(self, index, number):
        if index in self.dict1:
            num=self.dict1[index]
            self.dict2[num].remove(index)
            if len(self.dict2[num])==0:
                del self.dict2[num]
        self.dict1[index]=number
        if number not in self.dict2:
            self.dict2[number]=SortedSet()
        self.dict2[number].add(index)        

    def find(self, number: int) -> int:
        if number not in self.dict2:
            return -1
        elem=self.dict2[number].pop(0)
        self.dict2[number].add(elem)
        return elem


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
class Bitset:

    def __init__(self, size: int):
        self.size=size
        self.bitset0=set()
        for i in range(size):
            self.bitset0.add(i)
        self.bitset1=set()

    def fix(self, idx: int) -> None:
        if idx not in self.bitset1:
            self.bitset1.add(idx)
            self.bitset0.remove(idx)

    def unfix(self, idx: int) -> None:
        if idx not in self.bitset0:
            self.bitset0.add(idx)
            self.bitset1.remove(idx)

    def flip(self) -> None:
        self.bitset1,self.bitset0=self.bitset0,self.bitset1

    def all(self) -> bool:
        count=len(self.bitset1)
        if count==self.size:
            return True
        return False

    def one(self) -> bool:
        count=len(self.bitset1)
        if count>=1:
            return True
        return False

    def count(self) -> int:
        count=len(self.bitset1)
        return count

    def toString(self) -> str:
        bitstr=""
        for i in range(self.size):
            if i in self.bitset1:
                bitstr+="1"
            else:
                bitstr+="0"
        return bitstr


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
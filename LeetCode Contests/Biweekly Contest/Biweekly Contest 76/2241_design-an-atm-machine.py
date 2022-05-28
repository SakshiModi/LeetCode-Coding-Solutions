class ATM:

    def __init__(self):
        self.main_dict={20:0,50:0,100:0,200:0,500:0} 
        self.keys=[20,50,100,200,500]
    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.main_dict[self.keys[i]]+=banknotesCount[i]

    def withdraw(self, amount):
        sorted_keys=[500,200,100,50,20]
        ans=[]
        for notes in sorted_keys:
            required=amount//notes
            available=self.main_dict[notes]
            subtract=min(required,available)
            amount-=subtract*notes
            ans.insert(0,subtract)
            if amount==0:
                break
        else:
            return [-1]
        while(len(ans)!=5):
            ans.insert(0,0)
        for i in range(5):
            self.main_dict[self.keys[i]]-=ans[i]
        return ans


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
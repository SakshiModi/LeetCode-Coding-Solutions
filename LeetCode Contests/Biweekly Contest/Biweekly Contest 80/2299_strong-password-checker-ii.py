class Solution:
    def strongPasswordCheckerII(self, password):
        n=len(password)
        if n<8:
            #print("a")
            return False
        lst=[0,0,0,0]
        temp=password[0]
        for i in range(n):
            if i!=0 and temp==password[i]:
                #print("b")
                return False
            if ord(password[i])>=97 and ord(password[i])<=122:
                lst[0]=1
            elif ord(password[i])>=65 and ord(password[i])<=90:
                lst[1]=1
            elif password[i] in {'0','1','2','3','4','5','6','7','8','9'}:
                lst[2]=1
            elif password[i] in {'!','@','#','$','%','^','&','*','(',')','-','+'}:
                lst[3]=1
            temp=password[i]
        #print(lst)
        for i in lst:
            #print(i)
            if i==0:
                #print("c")
                return False
        return True
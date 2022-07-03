class validity:
    def check(self,str1):
        lst=[]
        brak={"(":")","{":"}","[":"]"}
        for i in str1:
            if i in brak:
                lst.append(i)
            elif len(lst)==0 or brak[lst.pop()]!=i:
                return False
        return len(lst)==0

print(validity().check("(){}[]"))
print(validity().check("({)}[]"))
print(validity().check("[]({}"))

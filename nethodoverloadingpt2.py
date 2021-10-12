class student:

    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
            return s
        elif a!=None and b!=None:
            s=a+b
            return s
        else:
            s=a
            return s

unicorn=student()
print(unicorn.sum(5))
print(unicorn.sum(2,8))
print(unicorn.sum(3,5,9))
print(unicorn.sum(1,4,7,8))
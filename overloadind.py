class Demo:

    def add(self,a,b):
        print(a+b)

    def add(self,a,b,c):
        print(a+b+c)
d1=Demo()
d1.add(1,2,8)


print ("python overloading")
#not like java only works second
class Demo:

    #make one arg as default
    def add(self,a,b,c=0):
        print(a+b+c)
d1=Demo()
d1.add(1,2)


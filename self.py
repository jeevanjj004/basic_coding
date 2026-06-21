class test_self():
    name=""
    sal=0
    def __init__(self,name):
        self.name=name
        self.sal=1000
t1=test_self('thomas')
print(t1.name,t1.sal)

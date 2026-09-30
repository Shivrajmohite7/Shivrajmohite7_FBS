class Emp:
    def __init__(self,id,name,sal):
        self.eid=id
        self._name=name
        self.__sal=sal

e1=Emp(101,"Muraj",50000)
print(e1.eid)        
print(e1._name)
print(e1._Emp__sal)

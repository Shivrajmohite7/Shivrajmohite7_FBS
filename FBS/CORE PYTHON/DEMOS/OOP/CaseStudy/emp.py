class Employee:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal

    def __str__(self):
        return f"Id={self.id}\t Name={self.name}\t Sal={self.sal}"

    def getId(self):
        return self.__id
    def setId(self,newId):
        self.__id=newId
    
    def getName(self):
            return self.__name
    def setName(self,newName):
        self.__name=newName

    def getSal(self):
            return self.__sal
    def setSal(self,newSal):
        self.__sal=newSal




# "python c:/Users/TUTION/Desktop/FBS/CORE PYTHON/DEMOS/OOP/CaseStudy/emp.py"
# python c:\Users\TUTION\Desktop\FBS>
# python "c:/Users/TUTION/Desktop/FBS/CORE PYTHON/DEMOS/OOP/CaseStudy/emp.py"

# python Desktop/FBS/CORE PYTHON/DEMOS/OOP/CaseStudy/emp.py"
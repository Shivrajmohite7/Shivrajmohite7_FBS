from emp import Employee

class Dev(Employee):
    def __init__(self, id, name, sal,bon):
        super().__init__(id, name, sal)
        self.__bon=bon

    def getBon(self):
        return self.__bon
    def setBon(self,newBon):
        self.__bon=newBon

    def __str__(self):
        return super().__str__()+f"\t Bonus={self.__bon}"
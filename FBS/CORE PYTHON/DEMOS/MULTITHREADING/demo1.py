from time import sleep
from threading import Thread

def fun1():
    for i in range(5):
        print("virat")
        sleep(1)
def fun2():
    for i in range(5):
        print("rohit")
        sleep(1)
def fun3(n):
    n=int(input("enter:"))
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        print(fact)
        sleep(1)

# x=fun3(120)
t1=Thread(target=fun1)
t2=Thread(target=fun2)
t3=Thread(target=fun3(30))

t3.start()
t3.join()
t1.start()
t2.start()

t1.join()
t2.join()
t3.join()


# from time import sleep
# from threading import Thread

# class Bank:
#     balance=1000
#     def withdraw(self,need_amt):
#         self.need_amt=need_amt
    
#     def amt_to_be_withdraw(self,amt_withd):
#         self.amt_withd=amt_withd
        
#     amt_withdraw=input("amount to be withdrawed"{self.amt_withd})
    
#     def __str__(self):
#         print(self.need_amt-self.amt_withd)

# c bank:
#     bank_bal=1000
#     def __init__(self,amt_with):
#         self.amt_with=amt_with
        
#     def cal(self):
#         balance=self.amt_with-x
    

# print("I am in thread")



# Python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/DEMOS/MULTITHREADING/demo1.py"
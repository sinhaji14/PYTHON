#hybridIn:- if more than one type of inheritance is implemented in the same code
class A:
    def method1(self):
        print("class A")
class B(A):
    def method2(self):
        print("class B")    
class C(A):
    def method3(self):
        print("class C")
class D(B,C):
    def method4(self):
        print("class  D")
d=D()
d.method1() 
d.method2()
d.method3()
d.method4()





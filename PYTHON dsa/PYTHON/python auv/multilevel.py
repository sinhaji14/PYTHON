class A():
      def f1(self):
          print("this is class A")
class B(A):
        def f2(self):
            print("this is class B")
class C(B):
         def f3(self):
             print("this is class C") 
d=C()
d.f1()
d.f2()
d.f3()
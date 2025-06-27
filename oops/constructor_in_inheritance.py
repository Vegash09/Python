class A:
    def __init__(self,name,age):
        self.name = name
        self.age = age


class B(A):
    def __init__(self,name,age,interest,hobby):
        super().__init__(name,age)
        self.interest = interest
        self.hobby = hobby

Vegash = B("Vegash",21,"Sports","Running")




class C:
    def __init__(self,first,second):
        self.first = first
        self.second = second

class D:
    def __init__(self,third,fourth):
        self.third = third
        self.fourth = fourth


class E(C,D):
    def __init__(self,first,second,third,fourth,fifth):
        C.__init__(self,first,second)
        D.__init__(self,third,fourth)
        self.fifth = fifth


no = E(1,2,3,4,5)
print(no.second)
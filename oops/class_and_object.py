class factory:
    total_emp = 150000           # class variable
    def __init__(self,name,age): # Constructor
        self.name = name         # instance variable
        self.age = age
    def info(self):              # class method
        print(self.name, self.age)
    @staticmethod
    def info():                  # static method but its overrides the class method
        print("Static method")

vegash = factory("vegash",21)
factory.info()


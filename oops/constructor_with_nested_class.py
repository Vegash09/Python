class car:
    def __init__(self,car_name,car_no):
        self.car_name = car_name
        self.car_no = car_no
        self.no_of_tools = self.toolkit()
    def info(self):
        print(self.car_name, self.car_no)


    class toolkit:
        def __init__(self):
            print("Creating Tools object inside car object")

audi = car("audi",1234)

from abc import ABC,abstractmethod
class Engine(ABC):
    @abstractmethod
    def fuel(self):
        pass


class car(Engine):
    def fuel(self):
        print("Diesel")

class bike(Engine):
    def fuel(self):
        print("Petrol")
    
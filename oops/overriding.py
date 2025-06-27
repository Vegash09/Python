class parent:
    def show(self):
        print("Parent")

class child(parent):
    def show(self):
        print("Child")


Vegash = child()
Vegash.show()
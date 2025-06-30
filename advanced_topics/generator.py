import sys
def gen():
    yield "Hello"
    print("Statment 01")
    yield "World"
    print("Statment 02")


it = gen()
print(next(it))
print(next(it))



num = 0
lst = [i for i in range(10000000)]
genrate = (num for i in range(10000000))
print(next(genrate))
print(next(genrate))
print(next(genrate))
print(next(genrate))
print(next(genrate))



print(sys.getsizeof(genrate))
print(sys.getsizeof(lst))

def helper(func):
    def inner(a,b):
        print("Decorator")
        func(a,b)
        print("Adding Features!....")
    return inner



@helper
def mul (a,b):
    print(a*b)
'''
mul = helper(mul)
mul(10,20)'''


mul(10,20)



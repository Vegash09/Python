try:
    a = int("abc")
except ValueError:
    print("Value error")
except TypeError:
    print("Type error")



try:
    f = open("file.txt")
except FileNotFoundError:
    print("File not found")
finally:
    print("Cleaning up")

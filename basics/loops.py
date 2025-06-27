for i in range(5):
    print(i)
for i in range(1, 10, 2):
    print(i)
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
for char in "Vegash":
    print(char)
for item in (1, 2, 3):
    print(item)
my_dict = {'a': 1, 'b': 2}
for key in my_dict:
    print(key)
for key, value in my_dict.items():
    print(key, value)
for value in my_dict.values():
    print(value)
for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)
names = ['a', 'b']
marks = [10, 20]
for name, mark in zip(names, marks):
    print(name, mark)


for i in range(3):
    for j in range(2):
        print(i, j)


for i in range(3):
    print(i)
else:
    print("Loop completed")


for i in range(5):
    if i == 3:
        break
    print(i)


for i in range(5):
    if i == 2:
        continue
    print(i)

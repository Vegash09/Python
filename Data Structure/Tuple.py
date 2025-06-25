# Find the index of an element in a tuple.
l =(1,2,3,4,5)
print(l.index(5))


# Unpack a tuple into individual variables.
l =(1,2,3,4,5)
a,b,c,d,e = l
print(a)


# Count the occurrences of an element in a tuple.
l = (4,6,7,8,12,45,2,54,22,22,4,6)
L = [0]*(max(l)+1)


for i in l:
    L[i] += 1

for i in range(0,len(L)):
    print(i,"Repeated",L[i])
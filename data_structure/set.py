#  Create a set with some numbers and print it.
S = {1,2,3,4,5,6,6,5,4,3}
print(S)

#  Add a new element to a set.
S.add(55)
print(S)

# Remove an element from a set using remove() and discard().
S.discard(66) # Safer for removing the element
# S.remove(66) Throw the error if not present
print(S)

# Check if an element exists in a set.
if 2 in S:
    print("Yes")


# Convert a list with duplicate elements into a set to remove duplicates.
t = [1,1,34,1,13,3,3,3,3,5,5,6,7,8]
s = set(t)
print(s)
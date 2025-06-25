# Find the second largest number in a list.
def secondLargest(L):
    tempList = sorted(L)
    return tempList[-2]

print(secondLargest([1,4,6,8,3,2]))


# Remove duplicates from a list while maintaining order.

def rem_dup(L):
    l = []
    for i in L:
        if i not in l:
            l.append(i)
    return l


print(rem_dup([1,1,2,4,4,3,3,7,8,5,1]))



# Check whether a list is a palindrome or not.

def ispali(L):
    start = 0
    end = len(L)-1
    while(start<end):
        if (L[start] != L[end]):
            return "Not Pali"
        start += 1
        end -= 1
    return "Pali"

print(ispali([1,2,1]))


# Find the common elements between two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
def common(list1,list2):
    l = []
    for i in range(0,len(list1)):
        for j in range(0, len(list2)):
            if list1[i] == list2[j]:
                l.append(list1[i])
    return l
print(common(list1,list2))
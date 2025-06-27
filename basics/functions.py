if __name__ == "__main__":
    print("Hi")

# Write a function to check if a number is prime.
def is_prime(num):
    for i in range(2,num):
        if (num%i) == 0:
            return "Not Prime"
    return "Prime"


print(is_prime(5))
print(is_prime(12))
print(is_prime(11))
print(is_prime(9))


#Write a function that returns the factorial of a given number.

def fact(num):
    if num == 1:
        return 1
    return num * fact(num-1)

print(fact(5))
print(fact(6))

#Write a function to check if a string is a palindrome.

def ispali(name):
    start = 0
    end = len(name)-1
    while(start<end):
        if(name[start] != name[end]):
            return "Not Pali"
        else:
            start += 1
            end -= 1
    return "Pali"

print(ispali("malayalam"))
print(ispali("vegash"))


# Write a function to count the number of vowels in a string.
def count_vowels(name):
    count = 0
    L = ['a','e','i','o','u','A','E','I','O','U']
    for i in name:
        if i in L:
            count += 1
    return count


print(count_vowels("Vegash"))


# Write a recursive function to generate the Fibonacci series up to n terms

def fibo(num):
    if num < 1:
        return 0
    if num == 1:
        return 1
    return fibo(num-1) + fibo(num-2)

print(fibo(10))
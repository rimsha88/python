# Function to reverse the digits of an integer
def intreverse(n):
    return int(str(n)[::-1])

# Function to check if brackets are matched
def matched(s):
    count = 0
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0

# Helper function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to sum all prime numbers in a list
def sumprimes(l):
    return sum(filter(is_prime, l))

# Examples to test the functions
print(intreverse(783))  # Output: 387
print(intreverse(242789))  # Output: 987242
print(intreverse(3))  # Output: 3

print(matched("zb%78"))  # Output: True
print(matched("(7)(a)"))  # Output: False
print(matched("a)(?"))  # Output: False
print(matched("((ijkl)78(A)&I(8(dd(FJ):);)?)"))  # Output: True

print(sumprimes([3, 1, 13]))  # Output: 19
print(sumprimes([2, 4, 6, 9, 11]))  # Output: 13
print(sumprimes([-3, 1, 6]))  # Output: 0
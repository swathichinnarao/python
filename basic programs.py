#1.Write a program to check if a number is a prime number
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Test the function
print(is_prime(29))  # Output: True
#2.Reverse a given number. For example, if the input is 12345, the output should be 54321.
def reverse_number(num):
    return int(str(num)[::-1])

# Test the function
print(reverse_number(12345))  # Output: 54321
#3.Find the largest of three numbers without using any library functions.
def largest_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

# Test the function
print(largest_of_three(10, 20, 15))  # Output: 20
#4.Write a program to calculate the factorial of a number using recursion.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Test the function
print(factorial(5))  # Output: 120
#5.Check if a given string is a palindrome.
def is_palindrome(s):
    return s == s[::-1]

# Test the function
print(is_palindrome("radar"))  # Output: True
print(is_palindrome("hello"))  # Output: False
#6.Write a program to calculate the sum of digits of a given number.
def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

# Test the function
print(sum_of_digits(1234))  # Output: 10
#7.Generate the Fibonacci sequence up to a given number ( n ).
def fibonacci(n):
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Test the function
print(fibonacci(50))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#8.Find the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Test the function
print(gcd(48, 18))  # Output: 6
#9.Check if a given number is an Armstrong number.
def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    power = len(digits)
    return num == sum(d ** power for d in digits)

# Test the function
print(is_armstrong(153))  # Output: True
print(is_armstrong(123))  # Output: False
#10.Write a program to find all prime numbers within a given range
def primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

# Test the function
print(primes_in_range(10, 50))  # Output: [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

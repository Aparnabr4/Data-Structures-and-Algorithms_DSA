# PROBLEM 1
# Do the factorial using recursive function

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)

print(factorial(4))


# PROBLEM 2
# Do Fibonacci series using recursive function
# Fibonacci: adding two previous numbers gives the next number

def fibo(n):
    if n <= 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)

for i in range(10):
    print(fibo(i), end=" ")


# PROBLEM 3
# Do Fibonacci series using for loop

def fi(n):
    a = 0
    b = 1
    for i in range(n):
        # print(a, end=" ")
        a, b = b, a + b

fi(10)


# PROBLEM 4
# Sum of all elements in an array -> iterative version

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def sum_of_all(arr):
    total = 0
    for n in arr:
        total += n
    return total

print(sum_of_all(arr))


# PROBLEM 5
# Multiplication of all elements in an array -> iterative version

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def mul_of_all_iter(arr):
    total = 1
    for n in arr:
        total *= n
    return total

print(mul_of_all_iter(arr))


# PROBLEM 6
# Multiplication of all elements in an array -> recursive version

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def mul_of_all(arr):
    if not arr:
        return 1
    return arr[0] * mul_of_all(arr[1:])

print(mul_of_all(arr))


# PROBLEM 7
# Sum of all elements in an array -> recursive version

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def summ_rec(arr):
    if not arr:
        return 0
    return arr[0] + summ_rec(arr[1:])

print(summ_rec(arr))

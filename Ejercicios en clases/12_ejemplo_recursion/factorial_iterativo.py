"""
Factorial de un numero mediante iteracion
"""

def factorial(n):
    factorial_final = 1
    while n > 1:
        factorial_final = factorial_final*n
        n = n - 1
    return factorial_final


print(factorial(5))
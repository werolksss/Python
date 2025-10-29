# Задание 1
def f(a, b):
    if b == 0:
        return a
    return f(b, a % b)

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def rev(num):
    if num < 10:
        return num
    return int(str(num % 10) + str(rev(num // 10)))

# Задание 2
def sum_rep(n, m, curr=None, s=1):
    if curr is None:
        curr = []
    if m == 1:
        if s <= n <= 9:
            print(curr + [n])
        return
    for i in range(s, 10):
        if i <= n:
            sum_rep(n - i, m - 1, curr + [i], i)

def double_fact(n):
    if n <= 1:
        return 1
    return n * double_fact(n - 2)

def count_ones(n):
    if n == 0:
        return 0
    return (n % 2) + count_ones(n // 2)

def add(a, b):
    if b == 0:
        return a
    return add(a + 1, b - 1)

def multiply(a, b):
    if b == 0:
        return 0
    return a + multiply(a, b - 1)

def is_palindrome(s, i, j):
    if i >= j:
        return True
    if s[i] != s[j]:
        return False
    return is_palindrome(s, i + 1, j - 1)

def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

print("НОД:", f(48, 18))
print("Фибоначчи 8:", fib(8))
print("Переворот 8223:", rev(8223))
print("Двойной факториал 7:", double_fact(7))
print("Единицы в 10:", count_ones(10))
print("Сложение 5+3:", add(5, 3))
print("Умножение 4*3:", multiply(4, 3))
print("Палиндром 'radar':", is_palindrome("radar", 0, 4))
print("Цифр в 12345:", count_digits(12345))
print("Представления 5 суммой 2:")
sum_rep(5, 2)
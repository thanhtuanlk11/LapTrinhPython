from importlib.abc import Finder
import math

# de quy
def Fibonacci(n):
    if n < 0: 
        print('số nhập không đúng')
    elif n == 0: 
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

n = int(input('Nhập n:'))
print('Số Fibonacci thứ n là: ', Fibonacci(n))


def sumOfnFibonacci(m):
    sum  = 0
    for i in range(m):
        sum += Fibonacci(i)
    return sum

m = int(input('Nhập m số Fibonacci:'))
print('Tổng n số fibonacci đầu tiên là: ', sumOfnFibonacci(m))



# khong dung de quy

def Fibonacci_1(n):
    a = 0
    b = 1
    if n < 0:
        print('Đầu vào không đúng')
    elif n == 0:
        return 0
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b
print('Số Fibonacci thứ n la: ', Fibonacci_1(n))

def sumOfnFibonacci_1(n):
    a = 0
    b = 1
    if n < 0:
        print('Incorrect Input')
    elif n == 0 or n == 1:
        return n
    else:
        s = 0
        while b <= n:
            s += b
            a, b = b, a + b
        return s

p = int(input('Nhập m số Fibonacci:'))
print('Tổng n số Fibonacci đầu tiên là ', sumOfnFibonacci_1(p))
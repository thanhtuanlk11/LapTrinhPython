import math
def check_perfect_square (m): 
    n = int(math.sqrt(m)) 
    return n * n == m 
def check_fibo(m): 
    check_perfect_square (5 * m * m + 4)
    check_perfect_square (5 * m * m - 4) 
    if ((n) == True): 
        print (n, "là số Fibonacci") 
    else: 
        print (n , "không phải là số Fibnacci")
n = int(input("Vui lòng nhập giá trị nguyên để kiểm tra số Fibonacci:")) 
check_fibo(n)



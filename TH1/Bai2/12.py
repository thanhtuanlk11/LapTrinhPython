import math
firts_list = [1,3,5,6,9,8,7,45,10,23,4,9,9,5,2,45,1]

list_prime = []
list_fibonacci = []
list_odd = []
def isOdd(x):
    return (x & 1)

def notDivisibleBy4():
    new_list = list(filter(lambda x: x % 5 != 0 and isOdd(x), firts_list))
    print('Số lẻ không chia hết cho 5 là : ', new_list)


def check_perfect_square(x):
    n = int(math.sqrt(x))
    return n * n == x

def check_fibonacci(a):
    return check_perfect_square(5 * a * a - 4) or check_perfect_square(5 * a * a + 4)
        

def printFibonacci():
    print('Số Fibonacci có trong mảng la:', end=' ')
    for i in firts_list:
        if check_fibonacci(i) == True:
            list_fibonacci.append(i)
    print(list_fibonacci , end=' ')


def check_prime_number(n):
    flag = 1
    if n < 2:
        flag = 0
        return flag
    for i in range(2, n):
        if n % i == 0:
            flag = 0
            break
    return flag

def check_prime_in_list():
    print('\nSố nguyên tố có trong mảng:', end=' ')
    for i in firts_list:
        if check_prime_number(i) == 1:
            list_prime.append(i)
    print(list_prime)

def find_prime_max():
    print('Số nguyên tố lớn nhất trong mảng:', max(list_prime))

def find_fib_min():
    print('Số Fibonacci nhỏ nhất là: ', min(list_fibonacci))

def average_odd():
    sum = 0
    average = 0
    for i in firts_list:
        if isOdd(i) == 1:
            list_odd.append(i)

    for i in list_odd:
        sum += i

    average = sum / len(list_odd)
    return average

def oddNumberNotDivisibleBy3():
    result = 1
    odd_Number_Not_DivisibleBy3 = list(filter(lambda x: x % 3 != 0, list_odd))
    for i in odd_Number_Not_DivisibleBy3:
        result *= i
    return result

def ChangeLocation(number1, number2):
    firts_list[number1], firts_list[number2] = firts_list[number2], firts_list[number1]
    return firts_list

def max2Number():
    current_list_sort = sorted(firts_list)
    print('Số lớn thứ 2 trong danh sách là : ', current_list_sort[-2])

def sumLastNumber():
    sum = 0
    for i in firts_list:
        sum = sum + i % 10
        i = int(i / 10)
    return sum

def countAppearsOfNumbers():
    n = int(input('Nhập sốc cần đếm số lần xuất hiện '))
    print('Số lần xuất hiện số {0} là: {1} lần'.format(n, firts_list.count(n) ))

def printNumberAppears():
    n = int(input('Nhập số lần xuất hiện của một số:'))
    for i in firts_list:
        if n == firts_list.count(i):
            print('Số xuất hiện số {0} lần là: {1}'.format(n, i))
            break

def countMaxAppearsOfNumbers():
    counter = 0
    num = firts_list[0]
    for i in firts_list:
        curr_frequency = firts_list.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            num = i
    return num
notDivisibleBy4()
printFibonacci()
check_prime_in_list()
find_prime_max()
find_fib_min()
print('Trung bình các số lẻ :', average_odd(), end=' ')
print('\nCác phần tử không chia hết cho 3: ', oddNumberNotDivisibleBy3())
number1 = int(input('Nhập số hạng đầu: '))
number2 = int(input('nhập số hạng thứ 2: '))
print('Danh sach ban dau', firts_list)
print('Danh sach sau khi swap', ChangeLocation(number1 - 1, number2 - 1))
firts_list.reverse()
print('Danh sách sau khi đảo ngược là :', firts_list)
print('Số lớn thứ nhì trong danh sách',max2Number())
print('Tổng chữ số còn lại ', sumLastNumber())
print('số lần xuất hiện của một số trong danh sách',countAppearsOfNumbers())
print('Số xuất hiện n lần trong danh sách',printNumberAppears())
print('Số xuất hiện nhiều nhất là:',countMaxAppearsOfNumbers())
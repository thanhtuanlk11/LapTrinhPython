from cmath import sqrt

def canBacHai(n):
    sum = 0
    for i in range(n):
        sum += sqrt(i)
    return sum

n = int(input('Nhập n số nguyên đầu tiên: '))
print('Tổng căn bậc 2 cua N so nguyên dương dầu tiên là: ', canBacHai(n))
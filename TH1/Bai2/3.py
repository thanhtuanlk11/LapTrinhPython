n = int(input('Nhập n: '))
for num in range(2,n+1):
    for i in range(2,num):
        if (num%i==0):
            break
    else:
        print(num)
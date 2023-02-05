a = int(input('Nhập 1 số n : '))

def GiaiThua(a):
    if a ==0 :
        return 1
    return a * GiaiThua(a -1)

print(GiaiThua(a))
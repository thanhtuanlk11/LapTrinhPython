x = int(input('Nhập số giây : '))
gio = x // 3600
x = x % 3600
phut = x // 60
x = x % 60
print('kết quả : ', gio,'giờ : ',phut,'phút : ',x , 'giây')
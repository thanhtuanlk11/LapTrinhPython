from datetime import datetime
from re import I
from traceback import print_tb
from zlib import DEF_BUF_SIZE


class SinhVien:
    truong ='Đại học Đà Lạt'

    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self.__maSo = maSo
        self.__hoTen = hoTen
        self.__ngaySinh = ngaySinh
    
    #cho phép truy xuất từ bên ngoài thông qua trường mã số
    @property
    def maSo(self):
        return self.__maSo

    @maSo.setter
    def maSo(self,maso):
        if self.laMaSoHopLe(maso):
            self.maSo = maso

    @property
    def hoTen(self):
        return self.__hoTen
    
    @hoTen.setter
    def hoTen(self,ten:str):
        self.__hoTen = ten
    
    @property
    def ngaySinh(self):
        return self.__ngaySinh

    #phương thức tĩnh: các phương thức không truy xuất gì đến thuộc tính, hành vi của lớp
    @staticmethod
    def laMaSoHopLe(maso : int):
        return len(str(maso)) == 7
    #ohuonwg thức của lớp chỉ truy xuất tới biến thành viên của lớp , không truy xuất tới thuộc tính riêng của lớp 
    @classmethod
    def doiTenTruong(self,tenmoi):
        self.truong = tenmoi
    #tương tự ghi đè phưởng thức tostring()
    def __str__(self) -> str:
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"
    #hành vi của đối tượng sinh viên
    def xuat(self):
        print(f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}")

class DanhSachSV:
    def __init__(self) -> None:
        self.dssv = []
    def themSinhVien(self, sv: SinhVien):
        self.dssv.append(sv)
    def Xuat(self):
        for sv in self.dssv:
            print(sv)
    
    def timSVTheomssv(self, mssv: int):
        return (sv for sv in self.dssv if sv.maSo == mssv)

    #Tìm sv theo mssv nếu có trả về vị trí sv đó
    def timVTSvTheoMssv(self,mssv: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == mssv:
                return i
        return -1
    
    def xoaSVTheoMssv(self, maSo:int) -> bool:
        vt = self.timVTSvTheoMssv(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True 
        else :
            return False
    
    #tim sinh vien tên nam 
    def timSVTheoTen(self,ten: str) -> list  :
        kq =[]
        for i in range(len(self.dssv)):
            if(self.dssv[i].hoTen.split(' ')[-1]) == ten:
                kq.append(self.dssv[i])
        return kq
    #tìm tất cả sinh viên sinh trước ngày  15/6/2000
    def timSvSinhTruocNgay(self, ngay: datetime) -> list:
        return [sv for sv in self.dssv if sv.ngaySinh < ngay]
    #Sắp xếp sv theo chiều tăng dần 
    def sortByNameUp(self):
        self.dssv.sort(key=lambda x: x.hoTen.split(' ')[-1], reverse=False)
    #Sắp xếp sv theo chiều giảm dần 
    def sortByNameDown(self):
        self.dssv.sort(key=lambda x: x.hoTen.split(' ')[-1], reverse=True)
        
sv1 = SinhVien(1957690, "Nguyễn Văn A", datetime.strptime("1/1/2005", "%d/%m/%Y"))
sv2 = SinhVien(1957613, "Nguyễn Văn C", datetime.strptime("2/2/2004", "%d/%m/%Y"))
sv3 = SinhVien(1951350, "Nguyễn Văn V", datetime.strptime("1/1/1998", "%d/%m/%Y"))
sv4 = SinhVien(1951270, "Nguyễn Văn B", datetime.strptime("2/2/1999", "%d/%m/%Y"))
sv5 = SinhVien(1957290, "Nguyễn Văn K", datetime.strptime("1/1/2002", "%d/%m/%Y"))
sv5 = SinhVien(1911170, "Nguyễn Văn Nam", datetime.strptime("25/10/2001", "%d/%m/%Y"))



dssv = DanhSachSV()
f = open("sinhvien.txt",'r',encoding="UTF-8")

for sv in f:
    maSo = sv.split(',')[0]
    hoTen = sv.split(',')[1]
    ngay = sv.split(',')[2].strip()
    ngaySinh = datetime.strptime(ngay, "%d/%m/%Y")
    svInFile = SinhVien(maSo, hoTen, ngaySinh)
    dssv.themSinhVien(svInFile)
# dssv.themSinhVien(sv1)
# dssv.themSinhVien(sv2)
# dssv.themSinhVien(sv3)
# dssv.themSinhVien(sv4)
# dssv.themSinhVien(sv5)
dssv.Xuat()

ms = 1957290
kq = dssv.timSVTheomssv(ms)
vt = dssv.timVTSvTheoMssv(ms)

if vt != -1:
    print(f"Sinh vien co ma so {ms} nam o vi tri thu {vt + 1} trong danh sach")
else:
    print(f"Sinh vien co ma so {ms} khong ton tai trong danh sach")

if dssv.xoaSVTheoMssv(ms):
    print(f"Da xoa sinh vien co ma so {ms} trong danh sach")
else:
    print(f"Khong xoa duoc vi mssv {ms} khong ton tai trong danh sach")

name = "Nam"
for sv in dssv.timSVTheoTen(name):
    print(f' sinh viên kiếm có tên nam là: \n{sv}')

date = datetime.strptime("15/6/2000","%d/%m/%Y")
print(f' sinh viên có ngày sinh trước {date} là: ')
for sv in dssv.timSvSinhTruocNgay(date):
    print(sv)

#Hàm sắp xếp danh sach sinh vien theo tên tăng dần
print("danh sách sinh viên sau khi được sắp xếp là :")
dssv.sortByNameUp()
dssv.Xuat()

print("danh sách sinh viên theo thứ tự giảm dần là : ")
dssv.sortByNameDown()
dssv.Xuat()

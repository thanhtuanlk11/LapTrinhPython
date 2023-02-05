from datetime import date, datetime


class SinhVien:
    def __init__(self, maSo: str, ht: str, ns: datetime) -> None:
        self.hoTen = ht
        self.mssv = maSo
        self.ngaySinh = ns

    def xuat(self):
        print(f"{self.mssv}\t{self.hoTen}\t{self.ngaySinh}")

@property
def maSo(self):
    return self.mssv

@maSo.setter
def maSo(self, ms:str):
    if self.laMsHopLe(ms):
        self.mssv = ms

@staticmethod
def laMsHopLe(self, mssv: str):
    return len(mssv) == 7

#@classmethod
#def doiTruong(self, tenMoi):

def __str__(self) -> str:
    return f"{self.mssv}\t{self.hoTen}\t{self.ngaySinh}"

class DSSV:
    def __init__(self) -> None:
        self.danhSachSv = []

    def themSV(self, sv: SinhVien):
        self.danhSachSv.append(sv)

    def xuat(self):
        for sv in self.danhSachSv:
            print(sv)

    def timSvTheoMs(self, ms: str) -> list:
        return [sv for sv in self.danhSachSv if sv.mssv == ms]

    def timVTSvTheoMs(self, ms: str) -> int:
        for i in range(len(self.danhSachSv)):
            if self.danhSachSv[i].mssv == ms:
                return i
        return -1

    #Xoa mssv, cho biet co xoa duoc hay khong
    def xoa(self, ms: str) -> bool:
        vt = self.timVTSvTheoMs(ms)
        if vt != -1:
            del self.danhSachSv[vt]
            return True
        else:
            return False
    #Tim tat ca sinh vien sinh truoc 15/8/1999
    def timSvSinhTruocNgay(self, ngay: datetime) -> list:
        kq = []
        for i in range(len(self.danhSachSv)):
            if self.danhSachSv[i].ngaySinh < ngay:
                kq.append(self.danhSachSv[i])
        return kq

    #Tim tat ca sinh vien ten Nam trong danh sach
    def timSvTheoTen(self, ten: str) -> list:
        kq =[]
        for i in range(len(self.danhSachSv)):
            if self.danhSachSv[i].hoTen.split(' ')[-1] == ten:
                kq.append(self.danhSachSv[i])
        return kq; 
            


sv1 = SinhVien(1957690, "Nguyễn Văn A", datetime.strptime("1/1/2000", "%d/%m/%Y"))
sv2 = SinhVien(1957690, "Nguyễn Văn C", datetime.strptime("2/2/2000", "%d/%m/%Y"))

dssv = DSSV()
dssv.themSV(sv1)
dssv.themSV(sv2)
dssv.xuat()
ms = "1967690"
kq = dssv.timSvTheoMs(ms)
vt = dssv.timVTSvTheoMs(ms)

if vt != -1:
    print(f"Sinh vien co ma so {ms} nam o vi tri thu {vt + 1} trong danh sach")
else:
    print(f"Sinh vien co ma so {ms} khong ton tai trong danh sach")

if dssv.xoa(ms):
    print(f"Da xoa sinh vien co ma so {ms} trong danh sach")
else:
    print(f"Khong xoa duoc vi mssv {ms} khong ton tai trong danh sach")



sv1.diemTB = 8.0

sv1.xuat()
sv2.xuat()

# print(sv1.diemTB)
# print(sv2.diemTB)
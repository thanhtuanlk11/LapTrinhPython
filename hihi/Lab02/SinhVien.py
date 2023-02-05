#vidu ke thua
from datetime import datetime
from tokenize import String
from unittest import result
from xmlrpc.client import DateTime


class SinhVien:
    truong = "Đai học Đà Lạt"
    def __init__(self, maSo: str , ht: str , ns: datetime) -> None:
        self.__hoTen = ht
        self.__mssv = maSo
        self.__ngaySinh = ns
    #get    
    @property
    def name(self):
        return self.__hoTen
    #set
    @name.setter
    def name(self, ten: str):
        self.__hoTen = ten
        
    @property
    def ngaySinh(self):
        return self.__ngaySinh
    
    @property  
    def maSo(self):
        return self.__mssv
    #set
    @maSo.setter
    def maSo(self, ms: str):
        if self.msHopLe(ms):
            self.__mssv = ms
    
    @staticmethod
    def msHopLe(ms: str):
        return len(ms) == 7
    
    @classmethod
    def doiTruong(self , tenMoi)  :
        self.truong = tenMoi 
       
    def xuat(self):
        print(f"{self.__mssv}\t{self.__hoTen}\t{self.__ngaySinh}")
        
    def __str__(self) -> str:
        return f"{self.__mssv}\t{self.__hoTen}\t{self.__ngaySinh}"
    
class DSSV:
    def __init__(self) -> None:
        self.danhSachSV = []
        
    def themSv(self, sv: SinhVien):
        self.danhSachSV.append(sv)
        
    def xuat(self):
        for sv in self.danhSachSV:
            print(sv)
            
    def timSvTheoMS(self, ms: str) -> list:
        return [sv for sv in self.danhSachSV if sv.maSo == ms]
    
    def timVTSVtheoMs(self, ms: str) -> int:
        for i in range(len(self.danhSachSV)):
            if self.danhSachSV[i].maSo == ms:
                return i
        return -1
#x0a sv
    def xoa(self, ms: str) -> bool:
        vt = self.timVTSVtheoMs(ms)   
        if vt != -1:
            del self.danhSachSV[vt]
            return True
        else:
            return False
        
#tim sv sinh trc 
    def timSVNgay(self, ngay: datetime) -> list:
        return[sv for sv in self.danhSachSV if sv.ngaySinh < ngay]
#tim sv ten     
    def timSVTen(self, tenn: str) -> list:
        return[sv for sv in self.danhSachSV  if sv.name.split(' ')[-1] == tenn]
    
#Sap Xep tang
    def xepTang(self):
        self.danhSachSV.sort(key=lambda x: x.name.split(' ')[-1], reverse=False)
#Sap xep giam
    def xepGiam(self):
        self.danhSachSV.sort(key=lambda x: x.name.split(' ')[-1], reverse=True)      
            
sv1 = SinhVien(1911160, "Phan Trung Kien", datetime.strptime("02/09/2001", "%d/%m/%Y"))
sv2 = SinhVien(2222222, "Nguyen A", datetime.strptime("2/7/2000", "%d/%m/%Y"))

dssv = DSSV()
dssv.themSv(sv1)
dssv.themSv(sv2)

dssv.xuat()

ms = 2222222

    
vt = dssv.timVTSVtheoMs(ms)
if vt != -1:
    print(f"Tim duoc sinh vien co ma so {ms}, o vi tri: ", vt + 1)
else:
    print("Khong tim thay sinh vien")


name = "Kien"
for sv in dssv.timSVTen(name):
    print(f"Sinh vien co ten {name}: ",sv)
  
    
ns= datetime.strptime("15/06/2001", "%d/%m/%Y")
for sv in dssv.timSVNgay(ns):
    print(f"Sinh vien sinh truoc ngay {ns}: ", sv)


f = open("D:\Python\Lab02\ex.txt", "r")
for i in f:
    maSo = i.split(',')[0]
    hoTen = i.split(',')[1]
    ngay = i.split(',')[2].strip()
    ngaySinh = datetime.strptime(ngay, "%d/%m/%Y")
    sv = SinhVien(maSo, hoTen, ngaySinh)
    dssv.themSv(sv)
dssv.xuat()

print("Sap xep tang dan: ")
dssv.xepTang()
dssv.xuat()

print("Sap xep giam: ")
dssv.xepGiam()
dssv.xuat()
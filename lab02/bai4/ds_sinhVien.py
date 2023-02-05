from dataclasses import dataclass
from datetime import datetime
import imp
from sinh_vien_chinh_quy import sinhVienChinhQuy
from sv_phi_chinh_quy import sinhVienPhiCQ
from sinh_Vien import sinhVien

class DanhSachSv:
    def __init__(self) -> None:
        self.dssv = []
        
    def themSV(self, sv: sinhVien):
        self.dssv.append(sv)
    
    def xuat(self):
        for sv in self.dssv:
            print(sv)
    
    def timSVTheoMs(self, ms: str):
        for i in range(len(self.dssv)):
            if self.dssv[i].mssv == ms:
                return i
        else:
            return -1
        
    def timTheoLoai(self, loai: str):
        if loai == "chinhquy":
            return [sv for sv in self.dssv if isinstance(sv, sinhVienChinhQuy)]
        return [sv for sv in self.dssv if isinstance(sv, sinhVienPhiCQ)]
    
    def timTheoDiemRenLuyen(self):
        for sv in self.dssv:
            if isinstance(sv, sinhVienChinhQuy):
                if sv.diemRL >= 80:
                    print(sv)
                    
    def timSvCDsinhTruoc(self):
        ngay = datetime.strptime("15/08/1999", "%d/%m/%Y")
        td = "Cao đẳng"
        for sv in self.dssv:
            if isinstance(sv, sinhVienPhiCQ):
                if sv.TrinhDo == td and sv._ngaySinh < ngay:
                    print(sv)
        


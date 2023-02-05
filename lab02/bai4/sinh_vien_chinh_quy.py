import datetime
from sinh_Vien import sinhVien


class sinhVienChinhQuy(sinhVien):
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime, diemRL: int) -> None:
        super().__init__(maSo, hoTen, ngaySinh)
        self.diemRL = diemRL
        
    def __str__(self) -> str:
        return super().__str__() + f"\t{self.diemRL}"
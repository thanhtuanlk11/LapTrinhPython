import datetime
from sinh_Vien import sinhVien


class sinhVienPhiCQ(sinhVien):
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime, trinhdo: str, tgdt: int) -> None:
        super().__init__(maSo, hoTen, ngaySinh)
        self.ThoiGianDaoTao = tgdt
        self.TrinhDo = trinhdo
        
    def __str__(self) -> str:
        return super().__str__() + f"\t{self.TrinhDo}\t{self.ThoiGianDaoTao}"
from datetime import datetime


class sinhVien:
    truong = "Đại học Đà Lạt"
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self._maSo = maSo 
        self._hoTen = hoTen 
        self._ngaySinh = ngaySinh
        
    @property
    def hoTen(self):
        return self._hoTen
    
    @hoTen.setter
    def hoTen(self, hoTen: str):
        self._hoTen = hoTen
        
    @property
    def mssv(self):
        return self._maSo
    
    @mssv.setter
    def mssv(self, ms: int):
        if self.KtMsHopLe(ms):
            self._maSo = ms
        
    @staticmethod
    def KtMsHopLe(ms: str):
        return len(ms) == 7
    
    def __str__(self) -> str:
        return f"{self._maSo}\t{self._hoTen}\t{self._ngaySinh}"
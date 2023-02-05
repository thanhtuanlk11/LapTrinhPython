import math
from tkinter import N
from Hinh_Hoc import hinhHoc
class hinh_Tron(hinhHoc):
    def __init__(self, banKinh: float) -> None:
        super().__init__(banKinh)  
    
    @property
    def banKinh(self):
        return self._canh
   
    def TinhDienTich(self)-> float:
        return self._canh * self._canh * math.Pi()

    def __str__(self) -> str:
        return(f"Hình tròn bán kính bằng {self._canh} có diện tích là{self.TinhDienTich()}") 
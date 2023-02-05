
from tokenize import Double
from Hinh_Chu_Nhat import hinhChuNhat


class hinhVuong(hinhChuNhat):
    def __init__(self, canh: float) -> None:
        super().__init__(canh,canh) 

    

    def __str__(self) -> str:
        return(f"Hình vuông canh bằng {self._canh} có diện tích là{self.TinhDienTich()}") 
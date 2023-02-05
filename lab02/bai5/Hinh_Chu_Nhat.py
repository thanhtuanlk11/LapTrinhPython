from asyncio import TimerHandle, proactor_events
from mimetypes import init
from tokenize import Double
from Hinh_Hoc import hinhHoc
class hinhChuNhat(hinhHoc):
    def __init__(self, chieuDai: float, chieuRong: float) -> None:
        super().__init__(chieuDai,chieuRong)
        self.__Rong = chieuRong

    

    @property
    def chieuRong(self):
        return self.__Rong
    def chieuDai(self):
        return self._canh
    
   
    def TinhDienTich(self)->float:
        return self._canh * self.__Rong

    def __init__(self) -> str:
        return(f"hình hcn có chiều dài là {self._canh}, chiều rông là {self.__Rong} có diên tích là{self.TinhDienTich()}")
    
  



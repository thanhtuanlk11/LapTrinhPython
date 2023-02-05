from asyncio import TimerHandle
from curses import can_change_color
from pyexpat.model import XML_CQUANT_NONE
from tokenize import Double
from urllib.parse import non_hierarchical


class hinhHoc :
    def __init__(self,canh : Double) -> None:
        self._canh = canh

    def __str__(self) -> str:
        return f"{self.canh}\t"

    def TinhDienTich(self,canh : float):
        pass






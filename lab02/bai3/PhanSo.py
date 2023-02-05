from re import U
from unittest import result


class PhanSo:
    def __init__(self):
        self.__tu = 0
        self.__mau = 1
        
    @property
    def tu(self):
        return self.__tu
    
    @tu.setter
    def tu(self, tu):
        self.__tu = tu
        
    @property
    def mau(self):
        return self.__mau
    
    @mau.setter
    def mau(self, mau):
        if(mau != 0):
            self.__mau = mau
        else:
            print("Mau so khong hop le")
        
    def xuat(self):
        print(f"{str(self.tu)}\{str(self.mau)}")
        
    def __str__(self) -> str:
        return f"{self.__tu}\{self.__mau}"
    
    def rutGon(self):
        if self.tu % self.mau == 0:
            self.tu / self.mau
        if self.tu > self.mau:
            for i in range(2, self.mau+1):
                if(self.tu % i ==0 and self.mau % i ==0):
                    self.tu = int(self.tu/i)
                    self.mau = int(self.mau/i)
        else:
            for i in range(2, self.tu+1):
                if(self.tu % i ==0 and self.mau % i ==0):
                    self.tu = int(self.tu/i)
                    self.mau = int(self.mau/i)
        return self.xuat() 
    
    def __add__(self, other):
        result = PhanSo()
        if self.mau == other.mau:
            result.tu = int(self.tu) + int(other.tu)
            result.mau = int(self.mau)
        else:
            result.mau = int(self.mau)*int(other.mau)
            result.tu = int(self.tu)*int(other.mau) + int(self.mau)*int(other.tu)
        return result
    
    def __multiadd__(self, other):
        if self.mau == other.mau:
            self.tu = int(self.tu) + int(other.tu)
            self.mau = int(self.mau)
            self.rutGon()
        else:
            self.mau = int(self.mau)*int(other.mau)
            self.tu = int(self.tu)*int(other.mau) + int(self.mau)*int(other.tu)
            self.rutGon()
        return self
    
    def __sub__(self, other):
        result = PhanSo()
        if self.mau == other.mau:
            if self.tu >= other.tu:
                result.tu = self.tu - other.tu
                result.mau = self.mau
            else: 
                print('Sô bị trừ phải lớn hơn số trừ')
        else:
            if self.tu*other.mau >= self.mau*other.tu:
                result.mau = self.mau*other.mau
                result.tu = self.tu*other.mau - self.mau*other.tu
            else: 
                print('Sô bị trừ phải lớn hơn số trừ')
        return result.xuat()
    
    def __mul__(self, other):
        result = PhanSo()
        result.tu = self.tu * other.tu
        result.mau = self.mau * other.mau
        return result.xuat()
    
    def __truediv__(self, other):
        result = PhanSo()
        result.tu = self.tu * other.mau
        result.mau = self.mau * other.tu
        return result.xuat()
    

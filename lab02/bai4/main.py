from datetime import datetime

from sinh_Vien import sinhVien
from sinh_vien_chinh_quy import sinhVienChinhQuy
from sv_phi_chinh_quy import sinhVienPhiCQ
from ds_sinhVien import DanhSachSv

# sv1 = sinhVienChinhQuy(1911170, "Nguyễn Hữu Thành Nam", datetime.strptime("02/09/2001", "%d/%m/%Y"), 80)
# sv2 = sinhVienChinhQuy(1945678, "Nguyễn Văn C", datetime.strptime("01/09/2002", "%d/%m/%Y"), 70)
# sv3 = sinhVienChinhQuy(1912345, "Trần Văn B", datetime.strptime("02/01/2001", "%d/%m/%Y"), 90)
# sv4 = sinhVienPhiCQ(2012345, "Phan Văn D", datetime.strptime("04/09/1999", "%d/%m/%Y"), "Cao đẳng", 2)
# sv5 = sinhVienPhiCQ(2034567, "Nguyễn E", datetime.strptime("01/05/1999", "%d/%m/%Y"), "Cao đẳng", 2)
# sv6 = sinhVienChinhQuy(1934567, "Trần F", datetime.strptime("05/09/1999", "%d/%m/%Y"), 60)
# sv7 = sinhVienPhiCQ(1945678, "Võ Q", datetime.strptime("06/07/2001", "%d/%m/%Y"),"Trung cấp", 2.5)
# sv8 = sinhVienPhiCQ(2045678, "Phạm V", datetime.strptime("03/04/2001", "%d/%m/%Y"), "Trung cấp", 2.5)

dssv = DanhSachSv()
# dssv.themSV(sv1)
# dssv.themSV(sv2)
# dssv.themSV(sv3)
# dssv.themSV(sv4)
# dssv.themSV(sv5)
# dssv.themSV(sv6)
# dssv.themSV(sv7)
# dssv.themSV(sv8)
dssv.readFile('sinhvien.txt')
dssv.xuat()

vt = dssv.timSVTheoMs(1911160)  
print(f"Sinh vien ở vị trí thứ {vt +1} trong danh sách" )
kq = dssv.timTheoLoai("chinhquy")
print("Danh sách sinh viên theo loại:   ")
for sv in kq:
    print(sv)
    
print("Sinh viên có điểm rèn luyện trên 80 là: ")
dssv.timTheoDiemRenLuyen()

print("Sinh viên có trinh độ Cao đẳng sinh truóc ngày 15/08/1999 là: ")
dssv.timSvCDsinhTruoc()

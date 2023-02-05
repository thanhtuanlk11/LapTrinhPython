from datetime import datetime

from sinh_vien_chinh_quy import SinhVienChinhQuy
from sv_phi_chinh_quy import SinhVienPhiCQ
from sinh_vien import SinhVien
from ds_sinh_vien import DanhSachSv

sv1 = SinhVienChinhQuy(1957690," Trần Văn A ", datetime.strptime("23/6/1999","%d/%m/%Y"),80)
sv2 = SinhVienChinhQuy(1957691," Nguyễn Văn C ", datetime.strptime("5/12/1999","%d/%m/%Y"),90)
sv3 = SinhVienPhiCQ(1957692," Trần Thị thu ", datetime.strptime("5/6/1998","%d/%m/%Y"),"cao đẳng",2)
sv4 = SinhVienPhiCQ(2000324," Trần Thanh Tâm ", datetime.strptime("21/9/2000","%d/%m/%Y"),"cao đẳng",2)
sv5 = SinhVienPhiCQ(2004544," Nguyễn Thanh Trà ", datetime.strptime("15/8/1999","%d/%m/%Y"),"Trung cấp",2.5)
sv6 = SinhVienChinhQuy(2004567," Trần Minh Cảnh ", datetime.strptime("5/6/2000","%d/%m/%Y"),60)


dssv = DanhSachSv()
dssv.themSV(sv1)
dssv.themSV(sv2)
dssv.themSV(sv3)
dssv.themSV(sv4)
dssv.themSV(sv5)
dssv.themSV(sv6)


dssv.xuat()

vt = dssv.timSVTheoMs(2000324)
print (f" Sinh viên ở vị trí thứ {vt + 1} trong danh sách ")

kq = dssv.timSvTheoLoai("chinhquy")
print("danh sách sinh viên theo loại : ")
for sv in kq:
    print(sv)
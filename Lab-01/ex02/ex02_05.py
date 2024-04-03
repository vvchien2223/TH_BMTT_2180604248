so_gio_lam = float( input("Hãy Nhập Số Giờ Làm: "))
luong_gio =float(input("Hãy Nhập Lương Mỗi Giờ: "))
gio_tieu_chuan= 44
gia_vuot_tieu_chuan = max(0,so_gio_lam-gio_tieu_chuan)
thuc_linh=gio_tieu_chuan*luong_gio+gia_vuot_tieu_chuan*luong_gio*1.5
print("Số Tiền Thực Lĩnh:  ",thuc_linh)
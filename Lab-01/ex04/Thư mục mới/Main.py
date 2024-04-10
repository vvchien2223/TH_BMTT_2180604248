from QLSV import QLSV
from SV import SV

qlsv =QLSV()

sinh_vien_1 = SV(1, "Nguyễn Văn A", "Nam", "Khoa Học Máy Tính", 4.5)
sinh_vien_2 = SV(2, "Trần Thị B", "Nữ", "Kỹ Thuật Phần Mềm", 8.3)
sinh_vien_3 = SV(3, "Lê Văn C", "Nam", "Kỹ Thuật Điều Khiển và Tự Động Hóa",6.9)

qlsv.xeploaihocluc(sinh_vien_1)
qlsv.xeploaihocluc(sinh_vien_2)
qlsv.xeploaihocluc(sinh_vien_3)

qlsv.listSV.append(sinh_vien_1)
qlsv.listSV.append(sinh_vien_2)
qlsv.listSV.append(sinh_vien_3)

while (1== 1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("\n****************MENU****************")
    print("\n**1.Thêm Sinh Viên.               **")
    print("\n**2.Cập Nhật Thông Tin Sinh Viên. **")
    print("\n**3.Xóa Sinh Viên Theo Id.        **")
    print("\n**4.Tìm Kiếm Theo Tên.            **")
    print("\n**5.Sắp Xếp Theo Điểm.            **")
    print("\n**6.Sắp Xếp Theo Chuyên Ngành.    **")
    print("\n**7.Hiển Thị Danh Sách.           **")
    print("\n**0.Thoát.                        **")
    print("\n************************************")
    key =int(input("Nhập Lựa Chọn: "))
    if(key==1):
        print("\n1.Thêm Sinh Viên.")
        qlsv.nhapSinhVien()
        print("\nThêm Sinh Viên Thành Công!")
    elif(key==2):
        if(qlsv.soluongSinhVien()>0):
            print("\n2.Cập Nhật Thông Tin Sinh Viên")
            print("\nNhập Id: ")
            Id=int(input())
            qlsv.updateSinhVien(Id)
        else:
            print("\nDanh Sách Sinh Viên Trống")
    elif(key==3):
        if(qlsv.soluongSinhVien()>0):
            print("\n3.Xóa Sinh Viên")
            Id = int(input("Nhập Id: "))
            if(qlsv.deleteById(Id)):
                print("\nXóa Sinh Viên Thành Công")
            else:
                print("\nSinh Viên Không Tồn Tại")
        else:
            print("\nDanh Sách Trống")
    elif(key==4):
        if(qlsv.soluongSinhVien()>0):
            print("\n4.Tìm Kiếm Theo Tên")
            name =input("Nhập Tên: ")
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh Sách Trống")
    elif(key ==5):
        if(qlsv.soluongSinhVien()>0):
            print("\n5.Sắp Xếp Theo Điểm")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh Sách Trống")
    elif(key==6):
        if(qlsv.soluongSinhVien()>0):
            print("\n6.Sắp Xếp Theo Tên")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh Sách Trống")
    elif(key==7):
        if(qlsv.soluongSinhVien()>0):
            print("\n7.Hiển Thị Danh Sách")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh Sách Trống")
    elif(key==0):
        print("\nBạn Chọn Thoát Chương Trình")
        break
    else:
        print("\nKhông Có Chức Năng Này",
              "Hãy Chọn Chức Năng Hợp Lệ")
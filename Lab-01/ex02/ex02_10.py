def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
input_string = input("Nhập Chuỗi: ")
print("Chuỗi Sau Khi Đảo Ngược ",dao_nguoc_chuoi(input_string))
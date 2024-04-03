def kiem_tra_so_nguyen_to(n):
    if n<1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

number = int(input("Nhập Số Cần Kiểm Tra: "))
if kiem_tra_so_nguyen_to(number):
    print(number,"Là Số Nguyên Tố")
else:
    print(number,"Không Phải Số Nguyên Tố")        
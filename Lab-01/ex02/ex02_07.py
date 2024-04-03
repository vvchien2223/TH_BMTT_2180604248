print("Nhập Các Dòng Văn Bản (done Để Kết Thúc): ")
lines = []
while True:
    line = input()
    if line.lower()=='done':
        break
    lines.append(line)
print("\nCác Dòng Đã Nhập Sau Khi Chuyển Thành In Hoa: ")
for line in lines:
    print(line.upper())
def chia_het_cho_5(so_nhi_phan):
    so_thap_phan=int(so_nhi_phan,2)
    if so_thap_phan % 5 ==0:
        return True
    else:
        return False
chuoi_nhi_phan = input("Nhập Chuỗi Nhị Phân (Tách Bởi Dấu ','): ")
so_nhi_phan_list = chuoi_nhi_phan.split(',')
so_chia_het_cho_5 = [so for so in so_nhi_phan_list if chia_het_cho_5(so)]
if len(so_chia_het_cho_5)>0:
    ket_qua=','.join(so_chia_het_cho_5)
    print("Các Số Nhị Phân Chia Hết Cho 5: ",ket_qua)
else:
    print("Không Có Số Nhị Phân Nào Chia Hết Cho 5!")

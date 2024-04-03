def dem_so_lan_xuat_hien(lst):
    count_dict={}
    for item in lst:
        if item in count_dict:
            count_dict[item]+=1
        else:
            count_dict[item]=1
    return count_dict

input = input("Nhập danh sách các từ: ")
world_list = input.split()

print("Số lần xuất hiện của các phần từ: ",dem_so_lan_xuat_hien(world_list))
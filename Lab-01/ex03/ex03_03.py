def tao_uple_tu_list(lst):
    return tuple(lst)
input_list = input("Nhập danh sách các số: ")
numbers = list(map(int,input_list.split(',')))
print("List: ",numbers)
print("Tuple từ List: ",tao_uple_tu_list(numbers))

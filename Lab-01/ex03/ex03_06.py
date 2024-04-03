def xoa_phan_tu(dictionary,key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False

my_dic = {'a':1,'b':2,'c':3,'d':4}
key_delete ='d'
result=xoa_phan_tu(my_dic,key_delete)
if result:
    print("Phần tử đã được xoá từ Dictionary: ",my_dic)
else:
    print("Không tìm thấy phần tử cần xoá!")
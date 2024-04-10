from SV import SV

class QLSV:
    listSV = []
    
    def generateID(self):
        maxId =1
        if(self.soluongSinhVien()>0):
            maxId =self.listSV[0]._id
            for sv in self.listSV:
                if(maxId<sv._id):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId
    
    def soluongSinhVien(self):
        return self.listSV.__len__()
    
    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập Chuyên ngành của sinh viên: ")
        diemTB = float(input("Nhập điểm của sinh viên: "))
        sv = SV(svId,name,sex,major,diemTB)
        self.xeploaihocluc(sv)
        self.listSV.append(sv)
        
    def updateSinhVien(self,Id):
        sv:SV = self.findById(Id)
        if(sv != None):
            name = input("Nhập tên sinh viên: ")
            sex = input("Nhập giới tính sinh viên: ")
            major = input("Nhập Chuyên ngành của sinh viên")
            diemTB = float(input("Nhập điểm của sinh viên: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB= diemTB
            self.xeploaihocluc(sv)
        else:
            print("Sinh vien có ID = {}","không tồn tại!".format(Id))
    def sortById(self):
        self.listSV.sort(key=lambda x:x._id,reverse=False)
    
    def sortByName(self):
        self.listSV.sort(key=lambda x:x._name,reverse=False)
    
    def sortByDiemTB(self):
        self.listSV.sort(key=lambda x:x._diemTB,reverse=False)
        
    def findById(self,Id):
        searchResult = None
        if(self.soluongSinhVien()>0):
            for sv in self.listSV:
                if(sv._id ==Id):
                    searchResult = sv        
        return searchResult
    
    def findByName(self,keyword):
        listSinhVien=[]
        if (self.soluongSinhVien()>0):
            for sv in self.listSV:
                if(keyword.upper() in sv._name.upper()):
                    listSinhVien.append(sv)
        return listSinhVien
    
    def deleteById(self,Id):
        isDeleted = False
        sv = self.findById(Id)
        if(sv!= None):
            self.listSV.remove(sv)
            isDeleted = True
        return isDeleted
    
    def xeploaihocluc(self, sv:SV):
        if(sv._diemTB >=8):
            sv._hocluc = "Giỏi"
        elif(sv._diemTB >= 6.5):
            sv._hocluc = "Khá"
        elif(sv._diemTB >= 5):
            sv._hocluc = "Trung Bình"
        else:
            sv._hocluc= "Yếu"
            
    def showSinhVien(self,listSinhVien):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}"
                .format("Id","Name","Sex","Major","DiemTB","HocLuc"))
        if(listSinhVien).__len__()>0:
            for sv in listSinhVien:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}"
                      .format(sv._id,sv._name,sv._sex,sv._major,sv._diemTB,sv._hocluc))
        print("\n")
        
    def getListSinhVien(self):
        return self.listSV
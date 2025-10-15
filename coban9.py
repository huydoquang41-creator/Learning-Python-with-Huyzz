#Kieu du lieu string trong python
a = 'xin chao'
print(type(a))

#Cong chuoi
s1="Xin chao"
s2=' Huy'
s3=s1 + s2
print(s3)
#chuoi nhieu dong
chuoi_nhieu_dong='''
Dong 1
Dong 2
Dong 3
'''
print(chuoi_nhieu_dong)

#Lap lai chuoi
chep_phat='Em hua lam bai tap day du \n'
chep_phat_10=chep_phat*10
print(chep_phat_10)

#Kiem tra chuoi co phai con cua chuoi khac
chuoi_1 = 'xin chao Huy'
chuoi_2 = 'Huy'
chuoi_3 = 'VN'
if chuoi_2 in chuoi_1:
    print(chuoi_2,"la chuoi con cua ",chuoi_1)
else:
    print(chuoi_2,"Khong la con cua ",chuoi_1)

if chuoi_3 in chuoi_1:
    print(chuoi_3,"la chuoi con cua ",chuoi_1)
else:
     print(chuoi_3,"Khong la con cua ",chuoi_1)

#Viet hoa chu dau cua chuoi
s='hom nay troi dep qua'
s = str.capitalize(s)
print(s)
#Viet hoa toan bo chuoi

print(s.upper())
#Viet thuong toan bo
s=s.lower()
print(s)

#Tim va Dem so luong chuoi con
s='lap trinh python la mot xu huong hien nay . Ban hoc lap trinh python.'
print(s.find("pythonx")) #Tra ve -1 neu khong tim thay,nguoc lai tra ve vi tri dau tien
print(s.find('python'))
print(s.count('python'))

#Thay the chuoi
s=s.replace('python','PYTHON')
print(s)

#Cat chuoi thanh 1 List
list1 = s.split(' ')
print(list1)

print(s[0:10])


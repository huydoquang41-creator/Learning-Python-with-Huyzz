#Tao list rong 
emptylist= []

#Tao ra 1 doi duong list
emptylist2=list()

print(emptylist)
print(emptylist2)

#Tao list co du lieu
color=["red","green","orange","yellow"]
print(color)

studentlist = ["an","binh",'ngan','vy']
#List co thu tu , vi tri duoc danh dau tu 0 , tu trai sang phai

print(studentlist[2])
print(studentlist[0])

# studentlist[x:y] => Lay ra [x:y)
print(studentlist[:])
print(studentlist[1:2])
print(studentlist[0:2])
print(studentlist[1:4])

#Them phan tu vao cuoi List
#Su dung append
studentlist.append('thien') 
print(studentlist)
#Su dung studentlist[len():] = [""]
studentlist[len(studentlist):] = ['thanh']
print(studentlist)
#Them vao truoc 1 phan tu
#Su dung student.insert(vi tri,'du lieu')
studentlist.insert(2 , 'ngoc')
print(studentlist)

#So luong phan tu co trong List
#Su dung len()
print('So luong sinh vien:',len(studentlist))

#Dem so luong phan tu trong List
#Su dung studentlist.count('')
print('Dem ngoc:',studentlist.count('ngoc'))
print('Dem thanh:',studentlist.count('thanh'))

#Kiem tra phan tu co ben trong List 
    #Su dung studentlist.in
if 'ngoc' in studentlist:
    studentlist.remove('ngan')
    print(studentlist)    

#Xoa 1 phan tu ra khoi danh sach List = du lieu
#Su dung studentlist.remove('')
studentlist.remove('binh')
print(studentlist)
#Xoa 1 phan tu ra khoi danh sach List = vi tri
#Su dung student.pop(Vi tri)
studentlist.pop(0)
print(studentlist)
studentlist.pop(1)
print(studentlist)

#Dao nguoc List
#Su dung student.reverse(None)
studentlist.reverse()
print(studentlist)

#Sap xep lai
#Su dung student.sort(None)
studentlist.sort()
print(studentlist)
#Tao 1 List number
number = [7,2,5,1,6,7,2,3,8,9]
number.sort()
print(number)
'''number.reverse()
print(number)
'''
#Sap xep nguoc
#Su dung number.sort(reverse=True)
number.sort(reverse=True)
print(number)

#Xoa sach du lieu trong List
studentlist.clear()
print(studentlist)


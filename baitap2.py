#Bai tap xac dinh tam giac , tinh chu vi va dien tich tam giac
'''Nhap 3 diem tren truc toa do Oxy
 1.Xac dinh 3 diem co tao thanh 1 tam giac hay ko
 2.Neu la tam giac :
    2.a Xuat ra chu vi tam giac
    2.b Xuat ra dien tich tam giac   
'''
import math
xA=float(input("Nhap vao xA ="))
yA=float(input("Nhap vao yA ="))
xB=float(input("Nhap vao xB ="))
yB=float(input("Nhap vao yB ="))
xC=float(input("Nhap vao xC ="))
yC=float(input("Nhap vao yC ="))
#Tinh do dai doan thang AB=sqrt((xA-xB)^2+(yA-yB)^2)
print("Tinh chu vi,dien tich co 3 diem A({0},{1}),B({2},{3}),C({4},{5})".format(xA,yA,xB,yB,xC,yC))
AB=math.sqrt((xA-xB)**2+(yA-yB)**2)
AC=math.sqrt((xA-xC)**2+(yA-yC)**2)
BC=math.sqrt((xB-xC)**2+(yB-yC)**2)

if AB+AC>BC and AB+BC>AC and AC+BC>AB:
    print("La tam giac")
    #Chu vi tam giac
    cv=AB+AC+BC
    print("Chu vi tam giac la :",cv)
    #Dien tich tam giac
    p=cv/2
    s=math.fabs(math.sqrt(p*(p-AB)*(p-AC)*(p-BC)))
    print("Dien tich tam giac la :",s)
else:
    print("Khong la tam giac")
 
"""
import math
x = float(input("nhap vao gia tri x ="))
y = float(input("nhap vao gia tri y ="))
#Tri tuyệt đối
print("|x| = ",math.fabs(x))
#Căn bậc 2
print("sqrt(x) = ",math.sqrt(x))
# x lũy thừa y
print("x^y =",math.pow(x,y))
#floor
print("tra ve gia tri nho hon hoac bang x la :",math.floor(x))
#ceil
print("tra ve gia tri lon hon hoac bang x la :",math.ceil(x))
"""

#Toán tử điều kiện ( toán tử ba ngôi )
"""
x = input("Nhap vao so nguyen :")
x = int(x)
kq="chan" if (x%2==0) else "le"
print(x,"la so")
"""

#Cau lenh dieu kien
x=int(input("Nhap vao so nguyen:"))
#vi du 1
if(x>=0):
    print(x,"la so duong")
#vi du 2
if x%2==0:
    print(x,"la so chan")
else:
    print(x,"la so le")
#vi du 3
if x>=9:
    print("Xep loai : Xuat xac")
elif x>=8:
    print("Xep loai : Gioi")
elif x>=7:
    print("Xep loai : Kha")
else:
    print("Xep loai : Trung binh")



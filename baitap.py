# #Nhap du lieu
# #import thu vien
# import math
# print("Giai phuong trinh ax^2+bx+c=0")
# a=float(input("Nhap a ="))
# b=float(input("Nhap b ="))
# c=float(input("Nhap c ="))
# print("{0}x^2+{1}x+{2}=0".format(a,b,c))
# if a!=0:
#     delta=b**2-4*a*c
#     if delta<0:
#         print("phuong trinh vo nghiem")
#     elif delta==0:
#         x=-b/(2*a)
#         print("co nghiem kep x1=x2=",x)
#     else:
#         x1=(-b+math.sqrt(delta))/(2*a)
#         x2=(-b-math.sqrt(delta))/(2*a)
#         print("x1={0} va x2={1}".format(x1,x2))
# else:
#     print("khong phai phuong trinh bac 2")
x = int(input())
if (x%2 == 0):
    print("Even")
else:
    print("Odd")
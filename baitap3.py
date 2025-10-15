#Chuyen doi so thap phan sang nhi phan
a = -1
while a<=0 :
    a = int(input('Nhap vao so nguyen a>0 ='))

ketQua = ''
while (a>0) :
    print("a%2 = ",a%2 )
    ketQua = str(a%2)+ketQua
    a = a//2
    print("a = ",a)

print('Ket qua = ',ketQua)



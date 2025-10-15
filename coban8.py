#Vong lap for
n=int(input("Nhap vao n phan tu : "))
#Vong lap tu 0 den <n
for i in range(n):
    print(i)
#Vi du tinh tong tu 0 cho den n
tong=0
for i in range(n+1):
    tong+=i
print('tong = ',tong)

#Vong lap for,co buoc tuy chinh
for i in range(0,10,2):
    print(i)
for i in range(10,0,-1):
    print(i)

color = ['red','green','orange']
#Vong lap for duyet cac phan tu
for i in color:
    print(i)

#Vong lap for duyet theo vi tri
for i in range(len(color)):
    print(color[0])

#Vong lap long nhau
for j in range(2,10,1):
    print('Bang cuu chuong',j)
    for i in range(1,11):
        print('{0} x {1} = {2} '.format(j,i,i*j))


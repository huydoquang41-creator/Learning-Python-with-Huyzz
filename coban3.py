#cac phep toan trong python
'''
1. phep cong:+
2. phep tru : -
3. phep nhan : *
4. phep chia : /
5. chia lay phan du : %
6. mu^ : **
7. chia lay phan nguyen : //
'''
"""
x=input("nhap gia tri x:")
y=input('nhap vao y:')
z=int(x)/int(y)
a=int(x)%int(y)
b=int(x)//int(y)
print("x/y co ket qua la:",z,"va phan du la",a)
print('x chia y co phan nguyen la:',b)
"""

a = input('nhap vao a :')
a=float(a)
b = input('nhap vao b :')
b=float(b)
print('{0}+{1}={2}'.format(a,b,a+b))
print('{0}-{1}={2}'.format(a,b,a-b))
print('{0}*{1}={2}'.format(a,b,a*b))
print('{0}/{1}={2}'.format(a,b,a/b))
print('{0}%{1}={2}'.format(a,b,a%b))
print('{0}**{1}={2}'.format(a,b,a**b))
print('{0}//{1}={2}'.format(a,b,a//b))

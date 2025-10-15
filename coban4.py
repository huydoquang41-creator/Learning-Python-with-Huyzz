#toan tu so sanh va logic trong python
'''
1. > : toán tử lớn hơn
2. < : toán tử nhỏ hơn
3. == : toán tử khác(= : gán giá trị)
4. != : toán tử khác hoặc không bằng
5. >= : lớn hơn hoặc bằng
6. <= : nhỏ hơn hoặc bằng
'''
#Ví dụ về so sánh toán tử
x=int(input('x = '))
y=int(input('y = '))
#true hoặc false
print('{0}>{1} la {2}'.format(x,y,x>y))
print('{0}<{1} la {2}'.format(x,y,x<y))
print('{0}=={1} la {2}'.format(x,y,x==y))
print('{0}!={1} la {2}'.format(x,y,x!=y))
print('{0}>={1} la {2}'.format(x,y,x>=y))
print('{0}<={1} la {2}'.format(x,y,x<=y))

'''
1. and : trả về giá trị True nếu tất cả là True
2. or : trả về giá trị True nếu ít nhất 1 toán hạng True
3. not : phủ định 
# True = False ; False = True
'''
#Ví dụ về logic
z = int(input('z = '))
print((x<y) and (y<z))
print((x<y) or (y<z))
print(not (x>z) )

print('{0}<{1} and {2}<{3} = {4}'.format(x,y,y,z,(x<y)and(y<z)))

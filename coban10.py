#Vong lap while
n = -1

while (n<=0):
    n = int(input('Nhap vao n :'))

i = 0
tong = 0
while (i<=n):
    tong+=i
    i+=1
print('Tong =',tong)

#Vong lap while voi else
j=0
while (j<=10):
    print(j, 'Ben trong vong lap ')
    j+=1
else:
    print(j,'Ben ngoai vong lap')

j=0
while (j<=10):
    print(j, 'Ben trong vong lap ')
    j+=1
    if j>=5 :
        break
        #Cat ngang vong lap
else:
    print(j,'Ben ngoai vong lap')
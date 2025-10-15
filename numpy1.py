#Khai bao thu vien numpy
import numpy as np

#Tao Numpy Arrays bang python list
np.array([1,2,3,4])
#Numpy chuyen kieu du lieu thap hon sang kieu du lieu cao hon
#vi du
print(np.array([3.14 , 4 , 5 , 6 ]))
#Ep kieu (dtype)
print(np.array([1,2,3,4],dtype = 'float32'))
#Co the gan np.array cho bien bat ki
a1 = np.array([1,2,3,4])
print(type(a1))
#List 2 chieu
a2 = np.array([[1,2,3],[4,5,6]])
print(a2)
print(type(a2))

#thuoc tinh shape : return cho bao nhieu cot bao nhieu dong
print('So cot va so hang cua mang a2 la :',a2.shape)
#2 dong 3 cot
#thuoc tinh ndim : So chieu cua mang
print('So chieu cua mang a2 la :',a2.ndim)
#thuoc tinh dtype : kieu du lieu cua phan tu
print('kieu du lieu ben trong mang la :',a2.dtype)
#thuoc tinh size : Tong thanh phan ben trong mang
print('So luong phan tu ben trong mang a2 la :',a2.size)

#Tao Numpy Arrays bang nhung ham co san " zeros , ones , full , arange , linspace "
#Ham zeros : Tao 1 bang toan so 0
#Tao bang 1 chieu bang zeros()
print(np.zeros(2,dtype="int"))
#Tao bang 2 chieu bang zeros(())
print(np.zeros((2,3),dtype="int64"))

#Ham ones : Bang toan so 1
print(np.ones((3,5),dtype='float'))

#Ham full : Tao mang theo y minh muon
print(np.full([3,5],8)) 

#Ham arange : Tao bang theo range(bat dau,ket thuc,buoc nhay) 
print(np.arange(0,20,2))

#Ham linspace : Tao mang chia doan ra = khoang cach (bat dau,ket thuc,khoang cach)
print(np.linspace(0,1,5))

#Ham random : Tao mang ngau nhien
#Seed : lam cho ham ngau nhien luon ra 1 gia tri
np.random.seed(0)
print(np.random.random([4,4]))
#np.random.normal : voi min = 0 va do lech chuan = 1 
print(np.random.normal(0,1,[3,3]))
#np.random.randint : 
print(np.random.randint(0,10,[4,5]))
#np.random.rand : 
print(np.random.rand(4,4))




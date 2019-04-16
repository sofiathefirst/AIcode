#_*_  coding: utf-8 _*_
# Author: waltsmith
# Date:2017-12-12


## zip()函数单个参数
print('=*'*10 + "zip()函数单个参数" + '=*'*10)
list1 = [1, 2, 3, 4]
tuple1 = zip(list1)
# 打印zip函数的返回类型
print("zip()函数的返回类型：\n", type(tuple1))
# 将zip对象转化为列表
print("zip对象转化为列表：\n", list(tuple1))


## zip()函数有2个参数
print('=*'*10 + "zip()函数有2个参数" + '=*'*10)
m = [[1, 2, 3],  [4, 5, 6],  [7, 8, 9]]
n = [[2, 2, 2],  [3, 3, 3],  [4, 4, 4]]
p = [[2, 2, 2],  [3, 3, 3]]
# 行与列相同
print("行与列相同:\n", list(zip(m, n)))
# 行与列不同
print("行与列不同:\n", list(zip(m, p)))


## zip()应用，也可以使用for循环+列表推导式实现
# 矩阵相加减、点乘
m = [[1, 2, 3],  [4, 5, 6],  [7, 8, 9]]
n = [[2, 2, 2],  [3, 3, 3],  [4, 4, 4]]
# 矩阵点乘
print('=*'*10 + "矩阵点乘" + '=*'*10)
print([x*y for a, b in zip(m, n) for x, y in zip(a, b)])
# 矩阵相加,相减雷同
print('=*'*10 + "矩阵相加,相减" + '=*'*10)
print([x+y for a, b in zip(m, n) for x, y in zip(a, b)])



## *zip()函数
print('=*'*10 + "*zip()函数" + '=*'*10)
m = [[1, 2, 3],  [4, 5, 6],  [7, 8, 9]]
n = [[2, 2, 2],  [3, 3, 3],  [4, 4, 4]]
print("*zip(m, n)返回:\n", *zip(m, n))
m2, n2 = zip(*zip(m, n))
print(m == list(m2) and n == list(n2))

#为什么 循环zip返回的对象 第一次有值，第二次就没有值了呢
#zip对象” 是一个迭代器。 迭代器只能前进，不能后退。
z =zip(m,n)
x1 = [x for x in z]

x2 = [x for x in z]
print('循环zip返回的对象 第一次有值，第二次就没有值\n',x1,'\n第二次\n',x2)
#可以看成是解压和压缩的区别，zip相当与压缩  zip（*）相当于解压

x=["a","1"]
y=["b","2"]
z = list(zip(x,y))
print (list(zip(x,y)))
print (list(zip(*z)))

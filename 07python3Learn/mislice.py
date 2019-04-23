def cnt(n):
    while 1:
            yield n
            n+=1

c = cnt(0)
'''
c[10:20]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'generator' object is not subscriptable
'''

import itertools
for x in itertools.islice(c,10,20):
    print('fisrt \n',x)

for x in itertools.islice(c,10,20):
    print('second \n',x)
#islice() 会消耗掉传入的迭代器中的数据。 必须考虑到迭代器是不可逆的
#迭代器和生成器不能使用标准的切片操作

#!/usr/bin/python3
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):#如果 __str__() 没有被定义，那么就会使用 __repr__() 来代替输出。
        return '({0.x!s}, {0.y!s})'.format(self)

_formats = {
    'ymd' : '{d.year}-{d.month}-{d.day}',
    'mdy' : '{d.month}/{d.day}/{d.year}',
    'dmy' : '{d.day}/{d.month}/{d.year}'
    }

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

def test():
	d = Date(2019,4,5)
	print(format(d))
	print(format(d,'mdy'))
	print(str(Pair(3,4)))
if __name__ == '__main__':	
	test()


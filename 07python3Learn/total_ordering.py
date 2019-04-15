#!/usr/bin/python3
from functools import total_ordering



@total_ordering
class House:
    def __init__(self, rooms,name='aa'):
        self.name = name
        #self.style = style
        self.rooms = rooms

    #@property
    #def living_space_footage(self):
        #return sum(r.square_feet for r in self.rooms)

    def __str__(self):
        return '{}:'.format(self.rooms)

    def __eq__(self, other):
        return self.rooms == other.rooms

    def __lt__(self, other):
        return self.rooms < other.rooms

def test():
	a = House(3)
	b = House(5)
	print(a==b, a<b,a>b)
if __name__ == '__main__':	
	test()

class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        print('rev',n)
        while n <= self.start:
            yield n
            n += 1
    # Reverse iterator
    #def __next__(self):

if __name__ == '__main__':	
	for rr in reversed(Countdown(30)):
		  print(rr)
	for rr in Countdown(30):
		  print(rr)


	a= Countdown(3)
	ait = iter(a)
	print( next(ait))
	print(next(ait))



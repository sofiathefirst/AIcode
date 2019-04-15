import time
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)

# Create and launch a thread
from threading import Thread

if __name__ == '__main__':	
	t = Thread(target=countdown, args=(10,),daemon=True)
	t.start()
	t.join()
	while True:
		time.sleep(2)
		if t.is_alive():
				pass
				print('Still running')
		else:
				print('Completed')
				break

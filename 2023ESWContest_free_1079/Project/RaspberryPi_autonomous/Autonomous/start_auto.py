import line
import drain
import threading

if __name__ == '__main__':
	
	thread1 = threading.Thread(target = line.tracking)
	thread2 = threading.Thread(target = drain.capture)
	thread2.start()
	thread1.start()

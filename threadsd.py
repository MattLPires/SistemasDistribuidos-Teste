import threading
import time

count = 0
materia = "Sistemas Distribuidos"
key = threading.Semaphore(1)

def fun1():
	global count
	global materia
	
	while (True):
		
		key.acquire()
		print("Impressora 1: " + materia[count])
		count = count + 1
		if count > len(materia) - 1: count = 0
		key.release()
		time.sleep(1)
		
def fun2():
	global count
	global materia
	
	while(True):
	
		key.acquire()
		print("Impressora 2: " +  materia[count])
		count = count + 1
		if count > len(materia) - 1: count = 0
		key.release()
		time.sleep(1)

t1 = threading.Thread(target=fun1)
t2 = threading.Thread(target=fun2)
t1.start()
t2.start()
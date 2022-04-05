import threading 
import time

startTime = time.time()
x = 0

def tarefa1() :
	global x
	while (x!=10):
		x+=1
		print("tarefa 1")
		time.sleep(1)

def tarefa2() :
	global x
	while (x!=10):
		x+=1
		print("tarefa 2")
		time.sleep(1)

threading.Thread(target=tarefa1).start()
tarefa2()

print("Tempo de execução: ", time.time() - startTime)

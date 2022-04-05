import multiprocessing

global r
r=multiprocessing.Value('i', 0)
r.value = 0

def calculo(x,n):
  global r
  for i in range (x,x+n):
    print(i)
    r.value = r.value + i
    for j in range (100):
      for k in range (100000):
          a = 1

if __name__ == '__main__':
  p1 = multiprocessing.Process(target=calculo , args = (0,50,))
  p2 = multiprocessing.Process(target=calculo , args = (50,50,))
  p1.start()
  p2.start()
  p1.join()
  p2.join()
  print()
  print(r.value)


import numpy as np
import time
import socket
import pickle
import sys
import particionar


HOST = sys.argv[1]
PORT = 5000

a = int(input("Digite o tamanho da matriz:"))
b = int(input("Digite quantas matrizes:"))

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

dest= (HOST , PORT)
for i in range(b):
	time.sleep(a/500)
	tempo = time.time()
	matriz = np.random.randint(10, size=(a,a))
	print(matriz)
	list = [matriz , tempo]
	list = pickle.dumps(list)
	fatias = particionar.fatias(list)
	if type(fatias[1])==bytes:
		tamanho=len(fatias)
		tamanho=pickle.dumps(tamanho)
		udp.sendto(tamanho,dest)
		for i in range(len(fatias)):
			udp.sendto(fatias[i],dest)
			time.sleep(0.003)
	if type(fatias)==bytes:
		udp.sendto (fatias,dest)
udp.close()

import numpy as np
import time
import socket
import pickle
import particionar
import sys


HOST = '' 
PORT = 5000 
HOST2 = sys.argv[1]
PORT2 = 6000
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
dest = (HOST2, PORT2)
udp.bind(orig)
pizza=[]
i = 0
while True:
	msg, cliente = udp.recvfrom(1024)
	pizza.append(msg)
	count = pickle.loads(pizza[0])
#	print(type(count))
	i += 1
	if type(count)!=int:
		inversa =np.round( np.linalg.inv(count[0]),2)
		determinante =  np.round(np.linalg.det(count[0]),2)
		list =[determinante,inversa, count[1]]
		print (list)
		pizza = []
		i = 0
		envia = pickle.dumps(list)
		udp.sendto (envia , dest)
	if (i-1) == count:
		del(pizza[0])
		pizza= particionar.agrupar(pizza)
		pizza = pickle.loads(pizza)
		inversa = np.round(np.linalg.inv(pizza[0]), 2)
		determinante =  np.linalg.det(pizza[0])
		list =[determinante, inversa,pizza[1]]
		print(list)
		count = 0
		pizza = []
		i = 0
		envia = pickle.dumps(list)
		envia = particionar.fatias(envia)
		tamanho = len(envia)
		tamanho = pickle.dumps(tamanho)
		udp.sendto(tamanho,dest)
		for z in range(len(envia)):
			udp.sendto(envia[z], dest)
			time.sleep(0.001)
udp.close()

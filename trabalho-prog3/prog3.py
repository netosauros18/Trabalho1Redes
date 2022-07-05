import socket
import pickle
import time
import particionar
HOST = ''
PORT = 6000
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
pizza = []
i=0
while True:
	msg, cliete= udp.recvfrom(1024)
	pizza.append(msg)
	count = pickle.loads(pizza[0])
	i+=1
	if type(count)!=int:
		total = time.time()- count[2]
		print('Determinante:')
		print(count[0])
		print('Inversa:')
		print(count[1])
		print('tempo:')
		print(total)
		i=0
		pizza = []
	if (i-1)==count:
		del(pizza[0])
		pizza = particionar.agrupar(pizza)
		pizza = pickle.loads(pizza)
		total = time.time()- pizza[2]
		print('Determinante:')
		print(pizza[0])
		print('Inversa:')
		print(pizza[1])
		print('tempo:')
		print(total)
		i=0
		pizza = []
udp.close()

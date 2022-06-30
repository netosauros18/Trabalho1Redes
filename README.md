<h1 align="center">Projeto(Trabalho utilizando socket para envio de dados)</h1>



Este projeto tem o intuito de realizar a comunicação de 3 máquinas através do socket, onde a máquina 1 define o tamanho e quantas matrizes serão enviadas, a máquina 2 realiza os cálculos de determinante e inversa e a máquina 3 exibe os resultados e o tempo levado para este processo. 






<h1 align="center">1 - Configurar IPs</h1>

Em 'prog1', na linha 9 do programa, deve-se colocar o IP local da maquina que ira rodar o 'prog2', na linha 9 do codigo 'prog2' deve-se colocar o IP da maquina que ira rodar 'prog3'.

<h1 align="center">2 - Sincronizar maquinas</h1>

Deve-se configurar a maquina que ira rodar o 'prog2' como um servidor NTP, e como clientes dela as maquinas de 'prog1' e 'prog3'.
Segue o link com tutorial simplificado para configurar servidor/cliente NTP >>>"https://pt.linux-console.net/?p=262"<<<.

<h1 align="center">3 - Rodar programas</h1>

Os programas devem ser rodados em maquinas da mesma rede, com o programa 2 e 3 rodando, execute o programa 1 e escolha a dimensao da matriz a ser enviada e a quantidade de matrizes, matrizes maiores que 250x250 possuem determinantes com valores que atingem o overflow dos 64bits que os calculos do numpy utilizam, funcionamento eficiente para matrizes ate 300x300.
Apos feito isso, o programa 2 ira calcular a determinante e a inversa desta matriz e o programa 3 ira exibir isto, juntamente com o tempo levado para ser feito isso com cada matriz enviada.








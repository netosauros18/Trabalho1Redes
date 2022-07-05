import numpy as np
import sys
import pickle as pk

def fatias(datab):

  if sys.getsizeof(datab) > 1024:
    fatias=[]  
    mut = (int(np.ceil(sys.getsizeof(datab)/1024)))
#    print(sys.getsizeof(datab),mut)

    tamanho_fatias=sys.getsizeof(datab[:(len(datab)//mut)])
    


    #corrige o fator divisor para garantir que pacotes < 1024#
    while tamanho_fatias > 1024:
        mut = mut+2
        tamanho_fatias=sys.getsizeof(datab[:(len(datab)//mut)])



    for i in range(mut):
          s1 = datab[(i)*(len(datab)//mut):(i+1)*(len(datab)//mut)]
          fatias.append(s1)
#          print(sys.getsizeof(s1))
    if i==(mut-1) and (i+1)*(len(datab)//mut)< len(datab):

            s1 = datab[(i+1)*(len(datab)//mut):]
 #           print(sys.getsizeof(s1))
            fatias.append(s1) 
    fim = fatias
  else:
    fim = datab
  return fim

def agrupar(fatias):
  if type(fatias)==list:
        for i in range(len(fatias)):
            if i == 0:
              fim = fatias[0]
            else:
              if fatias[i]!=fatias[i-1]:
                fim+=fatias[i]
  else:
    fim = fatias
  return (fim)



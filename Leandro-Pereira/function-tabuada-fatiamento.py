# criando função com parâmetros de tabuada .
def conjuntoTabuada(valor1,valor2):
 if ( valor1 < valor2):
  for h in range(valor1,valor2+1):
    for i in range(0,11):
      calcTabuada = h *i 
      print(' ',h,'X',i,'=',calcTabuada,' ')
    print('\n')
 else:
     print('O numero ',valor1,'tem que ser menor que ',valor2,' para mostrar o conjunto da tabuada ')
print('Digite o número da Tabuada :')
n = int(input())
print('Mostrar tabuada de ',n,' até número :')
n2 = int(input())
print('\n')
# Funçâo  tabuada criada,com finalidade de fatiamentodo de conjuntos de tabuadas .
conjuntoTabuada(n,n2)
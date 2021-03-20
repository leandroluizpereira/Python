# criando função tabuada
def tabuada(valor1,valor2):

 if ( valor1 < valor2):
  for h in range(valor1,valor2+1):
    for i in range(0,11):
      calcTabuada = h *i 
      print(' ',h,'X',i,'=',calcTabuada,' ')
    print('\n')
 else:
     print('o número do valor 1 tem que ser menor que valor 2 para fazer o fatiamento')

n = int(input('Conjunto de Tabuada de :'))
n2 = int(input('para :'))
print('\n')
# Funçâo  tabuada criada fazendo fatiamentodo de conjuntos de tabuadas exemplo  de tabuada valor1 á tabuada valor2) 
tabuada(n,n2)
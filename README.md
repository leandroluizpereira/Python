
#   Observaçôes importantes sobre a linguagem Python
 

 ## Declaraçâo para a variável 
  não e necessário colocar o tipo de dados para a variável, a indentificação e automática .
  ```python
  #Exemplo
  x = 30; # int
  frase = 'Leandro está estudando a linguagen python'  # String
  ligarCpu = true   # bool
  a = 3.4  # float
  ```
  ## Concatenaçâo da variável
  ```python 
  #Exemplo 
  nome = 'Leandro Luiz Pereira'
  linguagem ='Python'
  print(' '+nome+', acha a linguagem ',linguagem,' muito legal')
  ```
  nota-se que pode ser usados tando vírgula quanto o sinal de + para concatenaçâo.
  ## Operadores lógicos 
  ```Python
  a = 20
  b = 30
  x = 40
  y = 39
  #Exemplo: AND :
  if(a<b and x<y):
    print('As duas expressôes são verdadeiro')
  else:
    print('As duas expressões são  falsos')
  #exemplo: OR
  if(a<b or x<y):
     print('Um das expressão  são verdadeiro')
  else:
     print('As duas expressôes são falso')
    #Exemplo: com AND e NOT
  if(a>b and  not x<y):
    print('as duas expressâo são verdadeiro')
  else:
    print('as duas expresão são falso')
  ```
     
 
 ## Funçâo input () para entrada de dados do teclado
   O input ele pega as informações digitada do teclado e retorna o tipo para String, se caso queira colocar números tem 
   que fazer a conversão para o tipo  de dados inteiro e bem simples para fazer  no python,exemplo de algoritmo .
   ```python
   print('Digite um valor:')
   n = int(input())
   ```
 ## if ternário 
 ```python
 #exemplo:
 f = ( "Criança" if (idade < 12) else ("adolescente"  if (idade < 18) else ("adulto" if (idade < 60) else "Experiente")))
print(f)
```
 ## for 
 
 o laço de repetiçâo for no python o incremento é interno, ou seja não é preciso declarar na estrutura de repetiçâo o i++ ,e para iniciar a contagem tem que sempre usar o método range(), exemplo:
 
 ```python 
 for i in range(0,10):
    print(i)
 ```
 e para mexer no incremento:
 
 ```python
 for i in range(10,0,-1):
      print(i)
```
<strong>Teste de mesa:</strong> ele vai fazer a contagem de 10 até 1


## Sintaxe da linguagem "simples" 
 * não é necessario colocar ponto e vírgula 
 * pode ser aspas duplas e aspas simples

## Criação da linguagem python
A linguagem python foi lançado em 1991 por Guido van Rossum 
 
   

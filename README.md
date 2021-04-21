
# :books: Anotaçôes sobre a linguagem Python

## Ir direto a determinado assunto :

* :star: Básico
  * [Sobre a linguagem Python](#sobre)
  * [Declaraçâo de variável](#declaracaovariavel)
  * [Concatenaçâo de variável](#concatenacaovariavel)
  * [Interpolaçâo de variável](#interpolacaodevariavel)
  * [Operadores Aritméticos](#operadoresaritmeticos)
  * [Operadores lógicos](#operadoreslogicos)
  * [Funçâo de entrada - input () ](#funcaoinput)
  * [Edentaçâo Python](#edentacaopython)
  * [Desvio condicional If encadeado](#ifencadeado)
  * [Desvio condicional if ternário](#condicionalifternario)
  * [Estrutura for](#estruturafor)
  * [Estrutura de Dados - listas - array - dicionarios](#estruturadedados)
* :star::star: Intermediario
  * [Métodos](#metodos)
  * [Funções](#function)
* Orientação a objeto
  <!-- *   [Modificadores de acesso](#modificadores) -->
   *   [Método Construtor](#metodosConstrutor)
   *   [Encapsulamento](#encapsulamento)
   *   [polimorfismo](#polimorfismo)
  <!-- *   [herança](#heranca) -->
* Bibliotecas 
   *   [Request - web](#request)

<div id ='sobre'/>

<br>

#  Sobre a linguagem Python 

## Criação da linguagem 
A linguagem python foi lançado em 1991 por Guido van Rossum 

## Sintaxe da linguagem: "simples" 
 * não é obrigatório colocar ponto e vírgula.
 * as aspas são opicional pode ser dupla ou simples.
 * edentaçâo é obrigatório 


## Software ou site para práticar


| <div align=center> Software |  <div align=center>Site |  <div align=center>Autor|   <div align=center>   Classificaçâo            |
|--|--|--|--|
| <div align=center>:x: |<div align=center>[Colab](https://colab.research.google.com)|<div align=center> Google | <div align=center>:star::star::star::star::star:|
|  |  |  | <div align=center>:star::star::star:                                         |





 <div id='basico'/>
 
 
 
 # :star: Básico
 

 
 
  <div id='declaracaovariavel'/>
 
 ## Declaraçâo de variável
 
  não e necessário colocar o tipo de dados para a variável, a indentificação e automática .
  ```python
  #Exemplo
  x = 30; # int
  frase = 'Leandro está estudando os conceitos da linguagem python'  # String
  ligarCpu = 'true'   # bool
  a = 3.4  # float
  x = 3 # int
  ```
  <div id='interpolacaodevariavel'/>
  
  ##  Interpolação de Variável 
  ```python 
  #Exemplo 
  nome = 'Leandro Luiz Pereira'
  linguagem ='Python'
  print(' '+nome+', acha a linguagem ',linguagem,' muito relevante')
  ```
  nota-se que pode ser usado tando vírgula quanto o sinal de + para interpolação de variável.
  
  <div id='concatenacaovariavel'/>
  
  ## Concatenaçâo da variável 
  
  ```python 
  #Exemplo concatenaçâo de String
  nome = 'Leandro Luiz Pereira, '
  frase = 'está lendo os conceitos de '
  linguagem ='Python'
  concatenacao = nome + frase +  linguagem 
  print(concatenacao)
  ```
  
  
  <div id='operadoresaritmeticos'/>
  
  ## Operadores Aritméticos 
  ```Python
  #Exemplos:
  #para converter e somar as variável 
  a = 3.4
  x = 3
  y = float(x) + float(a)
  print(y)
  #método sum()
  b =[2,4,3,5,6]
  sum(b) 
  ```
 <div id='operadoreslogicos'/>
 
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
    print('As duas expressões são  falsa')
  #exemplo: OR
  if(a<b or x<y):
     print('Uma das expressões são verdadeiro')
  else:
     print('As duas expressôes são falsa')
    #Exemplo: com AND e NOT
  if(a>b and  not x<y):
    print('as duas expressâo são verdadeiro')
  else:
    print('as duas expresões são falso')
  ```
     
  <div id='funcaoinput'/>
  
 ## Funçâo input 
   O input ele pega as informações digitada do teclado e retorna o tipo para String, se caso queira pegar dígitos de números, tem 
   que fazer a conversão da variável para o tipo inteiro, e bem simples fazer esta conversão no python,exemplo:
   ```python
   print('Digite um valor:')
   n = int(input())
   ```
  <div id='edentacaopython'/>
  
## Edentaçâo Python
```python 
   
#Exemplo de edentaçâo com if 
a=2
if (a==2):
  # Espaço tab para estar dentro do if a==2
  print('a == 2 é verdadeiro')
  a=3
  #este if está dentro do if (a==2)
  if (a==3):
    #Espaço tab para estar dentro da instrução if a==3
    print(' a == 3 é verdadeiro')
    a=4
    b=3
    #este if está dentro do if (a==3)
    if (b == 3 and a == 4):
      print('    b == 3 and a == 4 que está dentro do if a == 3 e verdadeiro')
    else :
      print('   o valor b == 3 and a == 4 é falso')
  else:
    print(' a == 3 é falso')
  #este if está dentro do if (a==2)
  if (a==4):
    # Espaço tab para estar dentro comando de decisão if a==4
    print(' a == 4 é verdadeiro')
  else :
    print(' a == 4 é falso')
else:
  print(' O valor a == 2 é falso')
```

<div id='ifencadeado'/>

## Desvio condicional: if encadeado

```python 
# if composto: 
print('Digite um número de 1 a 4 ou número qualquer!')
a = int(input())
if (a == 2 ):
  print('if a == 2 true')
elif (a == 3):
  print('elif a == 3 true')
elif (a == 4):
  print('elif a == 4 é true')
else :
  print('if a == 2 e elif a == 3 e elif a == 4 são false')
```
<div id='condicionalifternario'/>

 ## Desvio condicional: if ternário 
 
 ```python
 #exemplo:
 f = ( "Criança" if (idade < 12) else ("adolescente"  if (idade < 18) else ("adulto" if (idade < 60) else "Experiente")))
 print(f)
 ```
 <div id="estruturafor">
 
  ## Estrutura for 
 
 o laço de repetiçâo for no python o incremento é interno, ou seja não é preciso declarar  o i++ , e para iniciar a contagem basta usar o método range(), exemplo:
 
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

 <div id ='estruturadedados'>
 
 ## Estrutura de Dados 
 
 ### Listas (list)
 
 ```python
 #Estrutura de dados - lista
#vetor  [indice 0] [indice 1] [indice 2] [indice 3]
nomes = ["Leandro"," Rita  ", " Luiz "," Pereira "]
#imprimir os dados 
print(nomes[0])
print(nomes[1])
print(nomes[0],nomes[2],nomes[3])

```
 nota-se que pode manipular a impressão de cada indice do vetor.
 
 Leitura da lista de  cada indice
 
```python
lista = ['0','1','2','3']
for x in lista :
  print('indice:',x)
```

 Leitura da lista de cada elemento do indice
```python
nome =["leandro","luiz","pereira"]
for aux in nome[2]:
 print(type(aux),aux)
 print(nome[0],nome[1],nome[2])
```
<strong>Teste de mesa:</strong>

```python
<class 'str'> p # indice [2]
<class 'str'> e # indice [2]
<class 'str'> r # indice [2]
<class 'str'> e # indice [2]
<class 'str'> i # indice [2]
<class 'str'> r # indice [2]
<class 'str'> a # indice [2]
leandro luiz pereira
```

### Dicionario

```python
dicionario = {"Cpf:":"999.999.999-99","nome:":"Leandro"}
dicionario ["cpf:"] = "888.888.888.-88"
print(dicionario)
for i in dicionario.items():
  print(i)
```

### Operaçôes com dicionários

```python
# incluindo dados no dicionário
# Primeira forma
aluno = {
'id':'1',
'nome': 'Leandro Luiz',
'idade':28,
'formacao':'Ciências da computaçâo'

aluno['AV1'] = 8.0
print(aluno)
}
#  update()
# Quando usa o update e  se o valor existir será atualizado, senão será criado
aluno.update( {'AV2': 7.5} )
print(aluno)
#Atualizar as notas AV1 para 6.0 e AV2 para 9.5

aluno.update({'AV1':6.0, 'AV2':9.5})
print(aluno)
```
### Percorrer lista do dicionario
```python

student = []
student.append({'name': 'Student 01','course': 'computer science','AV1':8 })
student.append({'name': 'Student 02','course': 'computer science','AV1':7 })
student.append({'name': 'Student 03','course': 'computer science','AV1':6 })
student.append({'name': 'Student 03','course': 'computer science','AV1':6 })
student.append({'name': 'Student 03','course': 'computer science','AV1':6 })


for dictionary in student: # percorrer a lista
  for student in [dictionary]: # percorre o dicionário
    print(student.get('AV1')) 
```

# :star::star: Intermediario 


<div id='metodos'>
 
## Métodos 
### Métodos que facilita a organização de listas
* count(<valor desejado>): Contar número de itens que possuem valor desejado.
* values(): verificar determinado valor
* items(): percorrer todas as chaves 
* append(<valor a ser adicionado>): Adicionar valor ao final da lista. 
* insert(<posiçaõ desejada>,<valor a ser adicionado>): Adicionar item numa posição específica.
* remove (<valor a ser removido>): Remover item de uma lista.
* sort(): Ordenar itens de uma lista. 
* len(<nome da lista>): Quantidade de itens que a lista possui. 
* Para alterar elemento de uma lista, pode-se alterá-lo diretamente pelo seu índice. 
* Para verificar se elemento pertence ou não a uma lista podemos usar: 
* IN = verificar se item pertence a lista. 
* NOT IN = verificar se item não pertence a lista.

```python
# Um exemplo de método de organização de lista : 
nome = ["Leandro", "Ricardo", "Monica"]
print("Nomes:\n", nome)
nome.append("Luiz")
if "Leandro" in nome:
    print("Leandro está na lista")
if "Marcus" not in nome:
    print("Marcus não está na lista")
```

<div id ='function' >
 
## Função (def)


```python
#Exemplo: criando funçâo tabuada , com parâmetro

def tabuada(numero):
  for i in range(0,11):
    tabuada = numero * i 
    print(' ',numero,' X ',i,' = ',tabuada,'')

tabuada(4)


```
<strong>Teste de mesa:</strong> 
    
  4  X  0  =  0 <br>
  4  X  1  =  4 <br>
  4  X  2  =  8 <br>
  4  X  3  =  12 <br>
  4  X  4  =  16 <br>
  4  X  5  =  20 <br>
  4  X  6  =  24 <br>
  4  X  7  =  28 <br>
  4  X  8  =  32 <br>
  4  X  9  =  36 <br>
  4  X  10  =  40 <br>
  
  
 ### Funçâo de procedimento
 ```python
 #exemplos de Funçôes de procedimento

def ascenderLuz():
  print('Luz acessa,com sucesso')

def apagarLuz():
  print('Luz apagada,com sucesso')

```
### Funçâo com retorno
```python
def multiplicacao(n1,n2):
  resultado = n1*n2
  return resultado
multiplicacao(3,5)
```  
<div id='modificadores'>
 
## Modificadores de acesso

<div id ='metodosConstrutor'>

## Método Construtor
```python
class EscolaParticular :
 # self faz referência ao atributo que está sendo manipulado
 # _init_ informa que esté método e o construtor
  def _init_ (self,cnpj,nome,cursos):
    self.cnpj = cnpj
    self.nome = nome
    self.cursos = cursos 
    self.media = 0
 ```

<div id ='encapsulamento'>
 
 ## Encapsulamento
 Protegendo os atributos .
 
```python
class Aluno :

#Métodos getters

def getNome(self):
    return self.nome

def getMatricula(self):
    return self.matricula

def getCurso(self):
    return self.curso
    
#Métodos setter
def setNome(self,nome):
    self.nome = nome 
  
def setMatricula (self,matricula):
    self.matricula = matricula
  
def setCurso (self,curso):
    self.curso = curso
```


<div id ='polimorfismo'>
 
## polimorfismo

<div id ='heranca'>
 
## herança

## Biblioteca 

<div id='request'>
 
## Request Web

## 1° testando requisiçâo

```python
import request
```

<p> Existem vários testes WEB que retornam informações e que são gratuitos.Como teste vamos utilizar o site PutsReq. Este site permite gravar solicitações HTTP e respostas pré-programadas para que possamos efetuar testes.</p>

[Link para o site : putsreq](https://putsreq.com/) <br>
Click em Create para ter o link de acesso a api <br>
depois :

```python
import requests
requisicao = requests.post("https://putsreq.com/[link de acesso]")
print(requisicao.text)
nome = input("informe seu nome: ")
requisicao = requests.post("https://putsreq.com/[link de acesso]?name="+nome)
print(requisicao.text)
```

## 2° fazendo requisiçâo de um site

para pesquisar conteudo e verificar em arquivo json : [omdbapi](http://www.omdbapi.com)

## Pegar informaçôes do site OMDBAPI 
* [link](http://www.omdbapi.com/apikey.aspx) acesse o link e cadastra-se, depois da verificação vai ser enviado  pelo e-mail a chave de acesso 

```python
import requests
import json
 
def omdbapi (titulo):
    requisicao = requests.post("http://www.omdbapi.com/?apikey=SuaChaveAqui="+titulo)
    return json.loads(requisicao.text)
 
filme = input("Nome do Filme em ingles (Braveheart): ")
if filme=="":
    filme = "Braveheart"
 
dicionario = omdbapi(filme)
print("\nOMDB")
if (dicionario["Response"]) == "False":
    print("Filme nao localizado")
else:
    print ("Ano de Produção:" +dicionario["Year"])
    print ("Genero: " + dicionario["Genre"])
    print ("Direção: " + dicionario["Director"])
    atores = dicionario["Actors"].split(", ")
    printouator = False
    for ator in atores:
        if not printouator:
            print ("Ator: " + ator)
            printouator = True
        else:
            print("    : " + ator) 
    ratings = dicionario["Ratings"]
    for rating in ratings:
        source = rating["Source"]
        value = rating["Value"]
        print("Fonte:",source+". Valor:",value)
```
O módulo json se faz necessário para que seja possível transformar a "string" de resposta da requisição WEB em um objeto Python, mas especificamente, dicionário.


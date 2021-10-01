# Variáveis

Python é uma linguagem dinamicamente tipada, ou seja, não é necessário declarar qual o tipo da varivável ou fazer *casting*, pois o Interpretador faz isso. Dessa modo, as variáveis são declaradas como no código abaixo:

```python
variavel = 'treinamento de python'
```
## Tipos de dado

### int

O tipo inteiro representa os números inteiros, sem um componente decimal.
```python
variavel = 10
```

### float

O tipo float representa os números racionais, ou seja, números que têm a parte decimal.

```python
variavel = 10.0
```

### complex

Representa os números complexos. Contém duas partes: a parte real e a parte imaginária, que recebe um "j" no sufixo.
A linguagem Python possui os seguintes tipos de dado.

```python
variavel = 10+5j
```

### string

Representa uma cadeia de caracteres. Pode ser declarado tanto com aspas duplas(""), quanto com aspas simples('').


```python
variavel = "teste"
variavel2 = 'testando'
```

### boolean

Representa um tipo de dado lógico que pode assumir dois valores: **true** ou **false**.

```python
variavel = true
variavel2 = false
```

### list

Agrupam um conjunto de elementos variados, são mutáveis e podem ser heterogêneas. São declaradas com a utilização de colchetes ([]).

```python
variavel = [10.0, 10, 'texto', 5+2j]
```

### tuples

Semelhante às listas, porém são imutáveis e são declaradas com a utilização de parentêses(()).


```python
variavel = (10.0, 10, 'texto', 5+2j)
```

### dicts

Dicionários armazenam um conjunto de elementos seguindo a lógica de chave-valor. São declarados com a utilização de chaves({}).

```python
variavel = {'inteiro': 10, 'float': 5.0, 'string': 'texto' }
```
### Outros
Existem ainda outros tipos, mostrados na tabela abaixo.

| **Tipo de dado**  | **Descrição**  | **Exemplo**  |
| ------------ | ------------ | ------------ |
| `str, unicode`  | Uma cadeia de caracteres imutável.  | `'teste', u'teste'`  |
| `list`  | Lista heterogênea mutável.  | `[4.0, 'string', True]`  |
| `tuple`  | Tupla imutável.  | `(4.0, 'string', True)`  |
| `set, frozenset`  | Conjunto não ordenado, não contém elementos duplicados.  | `set([4.0, 'string', True]), frozenset([4.0, 'string', True])`  |
| `dict`  | Conjunto associativo.  | `{'key1': 1.0, 'key2': False}`  |
| `int`  | Número de precisão fixa.  | `10` |
| `float`  | Ponto flutuante.  | `10.0` |
| `complex`  | Número complexo.  | `3+2j` |
| `bool`  | Booleano.  | `True or False` |

## Mudanças de tipo

Para efetuar mudança de tipo, é necessário fazer um *casting*.

### para string
```python
numero = 10 # a variável numero é um int

numero = str(numero) # mudança de tipo para string
```

### para int

```python
texto = '10' # a variável texto é uma string
texto = int(texto) # mudança de tipo para int
```

### para float

```python
texto = '27.5' # a variável texto é uma string
texto = float(texto) # mudança de tipo para float
```

### Verificar o tipo

Para verificar o tipo de uma variável se utiliza o *type()*.
```python
texto = '10'
print(type(texto)) # irá apresentar o tipo string na saída
```

# Operadores

A linguagem Python tem vários tipos de operadores, que são:

## Operadores aritméticos

São utilizados na execução de operações matemáticas.

```python
numero_1 = 7
numero_2 = 2

soma = numero_1 + numero_2
subtracao = numero_1 - numero_2
multiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2
divisao_inteira = numero_1 // numero_2
modulo = numero_1 % numero_2
exponenciacao = numero_1 ** numero_2

print(soma) # 9
print(subtracao) # 5
print(multiplicacao)  # 14
print(divisao) # 3.5
print(divisao_inteira) # 3
print(modulo)  # 1
print(exponenciacao) # 49
```

## Operadores de atribuição

Utilizados para atribuir valor a uma variável.

```python
var = 10
var += 5 # equivalente a var = var + 5
var -= 5 # equivalente a var = var - 5
var *= 5 # equivalente a var = var * 5
var /= 5 # equivalente a var = var / 5
var %= 5 # equivalente a var = var % 5
```

## Operadores de comparação

Utilizados para comparar valores. Retornam *true* ou *false*.

```python
var = 10

var == 10 # true
var < 10 # false
var > 10 # false
var != 10 # false
var >= 10 # true
var <= 10 # true
```
## Operadores lógicos

O *and* e o *or* são usados para unir duas ou mais expressões condicionais. O *not* é utilizado para negar o valor lógico de uma expressão.

```python
var = 10

var == 10 and var < 10 
var > 10 or var != 10 
not(var >= 10)
```

## Operadores de identidade

Servem para comparação de objetos.

```python
var = 10

var is 10
var is not 10
```
## Operadores de associação

Verificar se uma sequência contém um objeto.

```python
frutas = ["banana","laranja","uva","ameixa"]

fruta_1 = "ameixa"
fruta_2 = "melancia"

print(fruta_1 in frutas) # True
print(fruta_2 in frutas) # False
```

# Exemplo 1

Nesse exemplo, faremos um programa que receba o nome de um aluno e suas 4 notas bimestrais. Ao final, apresentar o nome junto a média anual.

O primeiro passo é receber a entrada do nome do aluno. Para isso utilizaremos o método *input()*.

```python
nome = input('Digite o nome do aluno: ')
```

Feito isso, agora receberemos as notas. Note que nessa parte é necessário fazer um *casting* das notas para *float*, pois o *input()* retorna um string. Dessa forma, será possível calcular a média.

```python
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))
```

Agora efetuaremos o cálculo da média.

```python
media = (nota1 + nota2 + nota3 + nota4)/4
```

Por fim, mostra-se os resultados. Lembrando novamente da necessidade de fazer o *casting*, agora de float para string.

```python
print('Nome: ' + nome)
print('Média: ' + str(media)) # casting de float para string
```

* * *
O próximo assunto a ser tratado será as [Estruturas de Controle de Fluxo](https://github.com/harielribeirof/treinamentoPython/blob/main/04%20-%20estruturas%20de%20controle%20de%20fluxo/condicional_repeticao.md).


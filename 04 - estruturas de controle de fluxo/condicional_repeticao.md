# Estruturas de controle de fluxo

## Indentação

Antes de prosseguir, é importante ressaltar a que o Python depende da indentação para definir os escopos no código, pois não há a utilização de ponto e vírgula. Ou seja, o código abaixo está incorreto:

```python
if a < b:
print(a)
```

Enquanto que o próximo está correto.


```python
if a < b:
    print(a)
```

## Comandos *if*

O *if* é a estrutura de controle mais comum. Verifica o valor booleano de uma expressão.

```python
x = 1
if x < 0:
    print('opção 1')
elif x == 0:
    print('opção 2')
elif x == 1:
    print('opção 3')
else:
    print('se não')
```

Podem haver vários *elifs* e apenas um *else*, sendo que este é opcional.

## Comandos *for*

Itera sobre os itens de qualquer sequência em ordem.


```python
lista = ['a', 'b', 'c']

for i in lista:
    print(i)

# SAÍDAS:   a
#           b
#           c
```

### Função *range()*

A função *range* é útil para percorrer sobre sequências numéricas.

```python
for i in range(4):
    print(i)

# SAÍDAS:   0
#           1
#           2
#           3
```
## Comandos *while*

Executa um conjunto de instruções, desde que uma condição seja satisfeita.

```python
i = 0
while i < 4:
  print(i)
  i += 1

# SAÍDAS:   0
#           1
#           2
#           3
```

## Comandos *break*, *continue* e a cláusula *else* nos laços de repetição

O comando *break* serve para sair imediatamente do laço de repetição mais interno.

```python
for i in range(4):
    if i == 3:
        break
    print(i)

# SAÍDAS:   0
#           1
#           2
```

Já o comando *continue* pula para a próxima iteração do laço.

```python
for i in range(4):
    if i == 2:
        continue
    print(i)

# SAÍDAS:   0
#           1
#           3
```

A cláusula *else* é executada sempre que o laço se encerra por exaustão do iterável (no caso do *for*) ou quando a condição se torna falsa (no caso do *while*), mas nunca quando o laço é interrompido por um break.

```python
for i in range(4):
    print(i)
    else:
        print('terminou')

# SAÍDAS:   0
#           1
#           3
#           terminou
```

O próximo assunto a ser tratado será [Funções](https://github.com/harielribeirof/treinamentoPython/blob/main/05%20-%20funcoes/funcoes.md).
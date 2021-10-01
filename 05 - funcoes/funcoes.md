# Funções

Funções em Python são definidas usando o *def*.

```python
def funcao():
    print('Isto é uma função!')
```

Para chamar uma função, usa-se o nome da função seguido de parênteses:

```python
def funcao():
    print('Isto é uma função!')

funcao()
```

## Argumentos

Os argumentos de uma função são passados após o nome da função, dentro do parênteses. O número de argumentos é de escolha do programador, desde que estejam separados por vírgulas.

```python
def soma(n1, n2):
    print(n1 + n2)

soma(10, 20)

# SAÍDA: 30
```
Os argumentos podem ser definidos com valores padrões. Dessa forma, uma função pode ser chamada com menos argumentos do que os que foram definidos.
```python
def soma(n1 = 5, n2 = 7):
    print(n1 + n2)

soma()

# SAÍDA: 12
```

### Argumentos arbitrários

Para casos em que não se sabe quantos argumentos são necessários, adiciona-se um `*` antes do nome do parâmetro. Nesse caso, a função irá receber uma tupla de argumentos.

```python
def funcao(*args):
    print(args)

funcao(1, 2, 3)

# SAÍDA: (1, 2, 3)
```

Ao utilizar `**` antes do nome do parâmetro, a função irá receber um dicionário de argumentos.

```python
def funcao(**kwargs):
    print(kwargs)

funcao(1, 2, 3)

# SAÍDA: {'um': 1, 'dois': 2, 'tres': 3}
```

## Retorno da função

Para definir o retorno de um função se usa o *return*.

```python


def funcao():
    return 5

print(funcao())

# SAÍDA: 5
```

## Comandos *pass*

Serve para marcar o fim de uma função ou estrutura de controle de fluxo. No caso das funções, é útil para criar uma função sem conteúdo.

```python
def funcao():
    pass
```

# Exemplo

Nesse exemplo, o usuário deverá fornecer um número inteiro e o programa deverá revertê-lo. Ou seja, ao inserir o número "123", o programa deve apresentar o número "321".

Para isso, criaremos a função *reverter()* que receberá como argumento um *int*.

```python
# Definir a função
def reverter(n):
    aux = ""            # variável auxiliar
    numero = str(n)     # casting do numero para string
    tam = len(str(n))   # guarda o tamanho da string do numero

    while(tam > 0):                 # laço para reverter o número
        aux = aux + numero[tam-1]
        tam -= 1
    return int(aux)     # retorno da função
```

O código acima irá utilizar três variáveis auxiliares: `aux` para receber o número revertido, `numero` para guardar a string que representa o número e por último `tam`, que irá guardar o tamanho da string.

Feito isso, cria-se um laço *while* para reverter o número, concatenando o último caractere de `numero` com `aux`. No final da função, há o retorno do número inteiro revertido.

```python
# Receber as entradas dos usuário
numero = input("Digite o número que deseja reverter: ")

# Chamar a função
numero = reverter(numero)

# Apresentar os resultados
print(numero)
```

Por fim, o programa deverá receber a entrada de um número inteiro do usuário, chamar a função e apresentar o resultado.
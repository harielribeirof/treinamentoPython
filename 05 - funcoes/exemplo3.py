
# Definir a função
def reverter(n):
    aux = ""            # variável auxiliar
    numero = str(n)     # casting do numero para string
    tam = len(str(n))   # guarda o tamanho da string do numero

    while(tam > 0):                 # laço para reverter o número
        aux = aux + numero[tam-1]
        tam -= 1
    return int(aux)     # retorno da função

# Receber as entradas dos usuário
numero = input("Digite o número que deseja reverter: ")

# Chamar a função
numero = reverter(numero)

# Apresentar os resultados
print(numero)
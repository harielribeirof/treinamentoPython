# Criação das variáveis
lista = []
par = 0
impar = 0

# Entradas
for i in range(10):
    lista.append(int(input('Digite um número inteiro: ')))

# Cálculo do número de pares e ímpares
for i in lista:
    if (i % 2) == 0:
        par += 1
    else:
        impar += 1

# Apresentar resultados
texto = 'Quantidade de {tipo}: {var}'

print(texto.format(tipo = 'par', var = par))
print(texto.format(tipo = 'ímpar', var = impar))

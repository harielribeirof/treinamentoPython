# Entrada do nome do aluno
nome = input('Digite o nome do aluno: ')

# Entrada das notas
nota1 = float(input('Digite a primeira nota: ')) # casting de str para float
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

# Cálculo da média
media = (nota1 + nota2 + nota3 + nota4)/4

# Apresentar resultados
print('Nome: ' + nome)
print('Média: ' + str(media)) # casting de float para string
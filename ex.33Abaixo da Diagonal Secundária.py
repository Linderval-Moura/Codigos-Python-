O = str(input())

linhas = 12
colunas = 12
matriz = []

for i in range(1, linhas):
  linha = []
  for j in range(1, colunas):
    numero = float(input())
    linha.append(numero)
  matriz.append(linha)
soma = 0  
soma_matriz = []

if O == 'S':
  for i in range(1, linhas):
    soma_matriz = []
    for j in range(linhas-1, colunas):
        soma += matriz[i][j]
    soma_matriz.append(soma)
  soma_total = sum(soma_matriz)
  print(soma_total)

elif O == 'M':
  aux = 0
  for i in range(1, linhas):
    soma_matriz = []
    for j in range(linhas-1, colunas):
        soma += matriz[i][j]
        aux += 1
    soma_matriz.append(soma)
    soma = sum(soma_matriz)
  media = soma/aux
  print('%.1f' %media)

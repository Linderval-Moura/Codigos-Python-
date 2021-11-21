# Inicio/Entradas 
distancia = float(input("Distancia percorrida em (km):"))
preco = float(input("Preço do combustível em (R$):")) 
consumo = float(input("Consumo de combustivel (km/l):"))

# Processamento
gasto = (distancia * preco) / consumo
consumo_combustivel = ("%.1f"%(gasto/preco))

# Saídas
print('Sua viagem é de {}km'.format(distancia))
print("Seu consumo medio é de:", consumo_combustivel, "Km/l")
print("Seu gasto medio é de: R$", gasto)

# Fim.



moedas = 0
capacidade = 100

while moedas < capacidade:
    qtd = int(input("Insira moedas"))

    if qtd > 2:
        continue 
    moedas += qtd
    print("quantidade de moedas =",moedas)

print("Quebrou o porco!")
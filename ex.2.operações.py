# Inicio/Entradas
numero1 = float(input(" Informe o primeiro nº real: "))
numero2 = float(input(" Informe o segundo nº real): "))

# Processamento
soma = ("%.1f"%(numero1 + numero2))
subtracao = ("%.1f"%(numero1 - numero2))
multiplicacao = ("%.1f"%(numero1 * numero2))
divisao = ("%.1f"%(numero1 / numero2))

# Saídas
print('Os números eram', numero1,"e", numero2)
print("O resultado das operações são: Soma =", soma)
print("Subtração =", subtracao," Multiplicação =", multiplicacao)
print("e Divisão =", divisao)

# Fim.

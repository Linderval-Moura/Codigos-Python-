carros = ["Ferrari Enzo", "VW Fusca", "Fiat Uno"]


carros.append("Audi A8")
carros.sort()

print (carros[:])

print("\nNOVO PROGRAMA!\n")

n1 = int(input('Digiti um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {},\n o produto é {} e\n a divisão é {:.3f}'.format(s, m, d))
print('Divisão inteira {} e\n potência {}'.format(di, e))

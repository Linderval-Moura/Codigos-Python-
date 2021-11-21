real = float(input('Quanto dinheiro você tem na carteora? R$'))
dolar = real / 5.31
euro = real / 6.28
print('Com R${:.2f} você pode comprar U${:.2f}'.format(real, dolar,))
print('Também com R${:.2f} você pode comprar €${:.2f}'.format(real, euro,))

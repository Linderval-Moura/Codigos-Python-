num1 = int(input("Digite um número inteiro:"))
num2 = int(input("Digite outro número inteiro:"))
num3 = int(input("Digite outro número inteiro:"))

if num1 > num2 and num1 > num3:
    maior = num1

elif num2 > num3:
    maior = num2
else:
    maior = num3

while True:
    if maior % num1 == 0 and maior % num2 == 0 and maior % num3 == 0:
        print(maior)
        break
    else:
        maior += 1


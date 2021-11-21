x = [int(i) for i in input().split()]

hinicial = x[0]
hfinal = x[1]

horaTotal = hfinal - hinicial

if horaTotal < 0:
    horaTotal += 24

if horaTotal == 0:
    print("O JOGO DUROU 24 HORA(S)")
else:
    print("O JOGO DUROU {} HORA(S)".format(horaTotal))

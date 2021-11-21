x = input().split()

hinicial = int(x[0])
minicial = int(x[1])
hfinal = int(x[2])
mfinal = int(x[3])

horaTotal = hfinal - hinicial
minutoTotal = mfinal - minicial

if minutoTotal < 0:
    minutoTotal += 60
    horaTotal -= 1
if horaTotal < 0:
    horaTotal += 24

if hinicial == 0 and minicial == 0:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    print('O JOGO DUROU %d HORA(S) E %d MINUTO(S)' %(horaTotal, minutoTotal))
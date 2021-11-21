n = int(input())


for e in range(1,n+1):
    leds = 0
    numero = input()

    for i in range(0,len(numero)):
        if numero[i] == '1':
            leds += 2
        if numero[i] == '2':
            leds += 5
        if numero[i] == '3':
            leds += 5
        if numero[i] == '4':
            leds += 4
        if numero[i] == '5':
            leds += 5
        if numero[i] == '6':
            leds += 6
        if numero[i] == '7':
            leds += 3
        if numero[i] == '8':
            leds += 7
        if numero[i] == '9':
            leds += 6
        if numero[i] == '0':
            leds += 6

    print('{} leds'.format(leds))
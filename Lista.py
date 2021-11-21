uma_lista = [3, 67, 56, 57, 3.14]

print(uma_lista[3])

print ("_" * 9)

for i in range(len(uma_lista)):
    print(i, uma_lista[i])

print ("_" * 12)

i = 0
n = len(uma_lista)
while (i < n):
    print(i, uma_lista[i])
    i += 1

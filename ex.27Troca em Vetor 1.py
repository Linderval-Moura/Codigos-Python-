#Faça um programa que leia um vetor N[20]. Troque a seguir, o primeiro elemento com o último, o segundo elemento com o penúltimo, etc., até trocar o 10º com o 11º. Mostre o vetor modificado.
N=[]

for i in range(20):
    x=int(input())
    N.append(x)

a=N[::-1]

for i in range(4):
    print('N[{}] = {}'.format(i,a[i]))

lista=[]

for i in range(10):
	
	entrada= int(input())
	
	if entrada<=0:
		lista.append(1)
	else:
		lista.append(entrada)

a=0
for i in lista:
	print('X[{}] = {}'.format(a, i))
	
	a += 1


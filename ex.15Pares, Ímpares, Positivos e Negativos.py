a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

t = [a,b,c,d,e]

posit = 0
negat = 0
impar = 0
par = 0

for n in t:
    if n > 0:
        posit += 1
    elif n != 0:
        negat += 1
    n = n % 2
    if n ==0:
        par += 1
    else:
        impar += 1
        
print ('{} valor(es) par(es)'.format(par))
print ('{} valor(es) impar(es)'.format(impar))
print ('{} valor(es) positivo(s)'.format(posit))
print ('{} valor(es) negativo(s)'.format(negat))

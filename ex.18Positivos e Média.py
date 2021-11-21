a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
t = [a,b,c,d,e,f]

posit = 0
media = 0

for n in t:
    if n > 0:
        posit += 1
        media += n

print('{} valores positivos'.format(posit))
print("{:.1f}".format(media / posit))

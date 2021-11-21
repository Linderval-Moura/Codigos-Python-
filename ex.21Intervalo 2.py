#URI Online Judge | 1072 Intervalo 2
n = int(input())

count = 0
count_2 = 0

for i in range(n):
  x = int(input())
  if(x >= 10) and (x <= 20):
    count += 1
  else:
    count_2 += 1

print('%d in\n%d out' %(count, count_2))

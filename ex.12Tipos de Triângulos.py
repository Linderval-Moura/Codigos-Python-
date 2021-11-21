x = input().split()
a = float(x[0])
b = float(x[1])
c = float(x[2])

if(a >= b) and (a >= c):
  cal = b + c
  if(a >= cal):
    print('NAO FORMA TRIANGULO')
  else:
    cal_2 = (b ** 2) + (c ** 2)
    if(a ** 2 == cal_2):
      print('TRIANGULO RETANGULO')
    elif(a ** 2 > cal_2):
      print('TRIANGULO OBTUSANGULO')
    else:
      print('TRIANGULO ACUTANGULO')
elif(b >= a) and (b >= c):
  cal = a + c
  if(b >= cal):
    print('NAO FORMA TRIANGULO')
  else:
    cal_2 = (a ** 2) + (c ** 2)
    if(b ** 2 == cal_2):
      print('TRIANGULO RETANGULO')
    elif(b ** 2 > cal_2):
      print('TRIANGULO OBTUSANGULO')
    else:
      print('TRIANGULO ACUTANGULO')
elif(c >= a) and (c >= b):
  cal = b + a
  if(c >= cal):
    print('NAO FORMA TRIANGULO')
  else:
    cal_2 = (b ** 2) + (a ** 2)
    if(c ** 2 == cal_2):
      print('TRIANGULO RETANGULO')
    elif(c ** 2 > cal_2):
      print('TRIANGULO OBTUSANGULO')
    else:
      print('TRIANGULO ACUTANGULO')
if(a == b) and (b == c):
  print('TRIANGULO EQUILATERO')
elif(a == b) or (b == c) or (c == a):
  print('TRIANGULO ISOSCELES')
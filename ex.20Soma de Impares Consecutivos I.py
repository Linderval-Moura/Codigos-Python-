x = int(input())
y = int(input())

count = 0

if(x % 2 == 0):
  for i in range(x, y, -1):
    if(i % 2 != 0):
      count += i
else:
  x -= 1
  for i in range(x, y, -1):
    if(i % 2 != 0):
      count += i
print(count)
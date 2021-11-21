def abc (w):
    return w*2

s = 0
x = int(input())
y = int(input())

for i in range(x, y):
    if (i%2 != 0):
        s += i*0.5

s = abc(s)
print(s)

    
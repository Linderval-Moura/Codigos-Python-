# Leia 3 valores inteiros e ordene-os em ordem crescente. 
x = input().split()
valores = [int(i) for i in x]

valores.sort()

print(*valores, sep='\n')
print()
print(*x, sep='\n')

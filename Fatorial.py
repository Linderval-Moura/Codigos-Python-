def fatorial(n):
    # Caso base: O fatorial de 0 é 1.
    if n == 0:
      return 1

    # O fatorial de um número n é: n * fatorial(n - 1).
    return n * fatorial(n - 1)


def fatorial2(n):
  fatorial = 1
  while (n):
    fatorial *= n
    n -= 1
  return fatorial
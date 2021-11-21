def fib(n):
    # Caso base: cálculo dos dois primeiros termos.
    if n <= 1:
        return n
    # Cálculo do n-ésimo termo.
    return fib(n - 1) + fib(n - 2)

def fib2(n):
    if n <= 1:
        return n
    fib_n_menos_2 = 0
    fib_n_menos_1 = 1
    for i in range(2, n):
        fib_n = fib_n_menos_1 + fib_n_menos_2
        fib_n_menos_2 = fib_n_menos_1
        fib_n_menos_1 = fib_n
    return fib_n_menos_1 + fib_n_menos_2
    
# Implementa la función fib(n) que retorna el n-ésimo número de la serie
# de Fibonacci:
# fib(1) = 1
# fib(2) = 1
# fib(n) = fib(n - 1) + fib(n - 2), para todo n > 2.


def fib(n):
    his = []
    a, b = 0,1
    while len(his) < n -1:
        if len(his) < 10:
            print(b, end=', ')
        a, b = b, a+b
        his.append(b)
    return "La secuencia Fibonacci de {}, es {}".format(n, b)



if __name__ == "__main__":
    # Prueba de la función: imprime los primeros 10 números en una línea
    # separados por coma y espacio.
    prueba_fib = ''
    print(prueba_fib)

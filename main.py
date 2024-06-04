#!/usr/bin/python3
import time
from functools import lru_cache
iteraciones = 100

# comentar la siguiente línea para probar la función
@lru_cache
def  fibo(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibo(n -1) + fibo(n-2)


def test_de_funcion(numiteraciones):
    tiempo_inicio = time.time()
    
    for i in range(0, numiteraciones):
        print(f'{i}: {fibo(i)}')

    tiempo_fin = time.time()
    print(tiempo_fin - tiempo_inicio)
    
    
tf = test_de_funcion
tf(iteraciones)

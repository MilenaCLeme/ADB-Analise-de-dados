"""
27. **Função de Memoização para Fatorial**:
    - Crie uma função chamada `memoFatorial` que usa memoização para otimizar o cálculo do fatorial.
"""

"""
Um feito com biblioteca 

from functools import lru_cache

@lru_cache(maxsize=None)
def memoFatorial(n):
    return n * memoFatorial(n-1) if n > 1 else 1
"""

def memoFatorial(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = n * memoFatorial(n - 1, memo)
    return memo[n]

print(memoFatorial(5))
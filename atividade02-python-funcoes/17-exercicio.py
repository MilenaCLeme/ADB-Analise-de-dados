"""
17. **Função para Converter Fahrenheit para Celsius**:
    - Crie uma função chamada `fahrenheitParaCelsius` que receba uma temperatura em Fahrenheit e retorne a temperatura convertida para Celsius.
"""

def fahrenheitParaCelsius(f):
    return round((f - 32) * 5/9, 2)

print(fahrenheitParaCelsius(77))
print(fahrenheitParaCelsius(60))
print(fahrenheitParaCelsius(40))

"""

25.0
15.56
4.44

"""
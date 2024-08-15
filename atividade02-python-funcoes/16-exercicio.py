"""
16. **Função para Converter Celsius para Fahrenheit**:
    - Crie uma função chamada `celsiusParaFahrenheit` que receba uma temperatura em Celsius e retorne a temperatura convertida para Fahrenheit.
"""

def celsiusParaFahrenheit(celsius):
    return round((9/5 * celsius) + 32, 2)

print(celsiusParaFahrenheit(21))
print(celsiusParaFahrenheit(18))
print(celsiusParaFahrenheit(22))

"""

69.8
64.4
71.6

"""
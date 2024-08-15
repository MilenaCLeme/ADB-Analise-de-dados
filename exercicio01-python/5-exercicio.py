"""

5. Classificação e Ajuste de Salário com Reajuste
   **Problema:** Crie um programa que receba o salário de um funcionário e determine sua faixa salarial: "Baixa" (até R$ 2.500), "Média" (de R$ 2.501 a R$ 5.000) ou "Alta" (acima de R$ 5.000). Aplique um reajuste de 7% para a faixa baixa, 5% para a faixa média e 3% para a faixa alta. Mostre o salário reajustado.

"""

print("Classificação e Ajuste de Salário com Reajuste")
faixa_salarial = lambda x: 'Alta' if 5000 < x else ('Média' if 2501 < x < 5000 else 'Baixa')

reajuste_faixa = lambda y: 1.03 if y == 'Alta' else (1.05 if 'Media' == y else 1.03)

def verificar_faixa_e_calcular_reajuste(salario):
    faixa = faixa_salarial(salario)
    reajuste = reajuste_faixa(faixa)
    return f"O salario R$ {round(salario, 2)} está na faixa {faixa} e o reajuste foi {round((salario * reajuste), 2)}"

salario = float(input("Digite um salario: "))

print(verificar_faixa_e_calcular_reajuste(salario))


"""

Classificação e Ajuste de Salário com Reajuste
Digite um salario: 5450
O salario R$ 5450.0 está na faixa Alta e o reajuste foi 5613.5

Classificação e Ajuste de Salário com Reajuste
Digite um salario: 2800
O salario R$ 2800.0 está na faixa Média e o reajuste foi 2884.0

Classificação e Ajuste de Salário com Reajuste
Digite um salario: 1500
O salario R$ 1500.0 está na faixa Baixa e o reajuste foi 1545.0

"""
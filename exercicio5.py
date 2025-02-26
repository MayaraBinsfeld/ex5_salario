"""
Programa: ex5_salario
Descrição: Este programa calcula o salário de um professor na universidade XYZ.
Autor: Mayara Binsfeld
Data: 25/02/2025
Versão: 0.0.1
"""


# Alocação de memória 

horas_trabalhadas = 0 
salario_bruto = 0
salario_liquido = 0
total_de_descontos = 0 

# Entrada de dados

horas_trabalhadas = int(input("Quantas horas foram trabalhadas?"))

# Processamento de dados

salario_bruto = horas_trabalhadas*40
total_de_descontos = salario_bruto*(3/10)
salario_liquido = salario_bruto - total_de_descontos

# Saída de dados

print(f"O salário bruto é {salario_bruto}, sendo os descontos {total_de_descontos}, e o salário líquido {salario_liquido}.")
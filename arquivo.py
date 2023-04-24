'''
    Cidade A: 80.000 e cresce todo ano 3% (0.03) => soma pelo todo 1.03
    Cidade B: 200.000 e cresce todo ano 1.15 (0.015) => soma pelo todo 1.015
'''

# Valores iniciais do ano
cidadeA = 80000
cidadeB = 200000

# Contador para começar o ano
i = 0

while cidadeA <= cidadeB:
    cidadeA *= 1.03
    cidadeB *= 1.015
    i += 1

print(f"O ano em que a Cidade A passará a cidade B é ano ano de {i}")

# Para igualar as cidades, tira o =, só deixa o menor
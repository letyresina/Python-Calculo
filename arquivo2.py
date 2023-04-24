# Ano de investimento
mesesInvestidos = 24
# Ano inicial 
i = 0
# Pra fazer a soma da taxa
soma = 0
# Variáveis iniciais
saldoInicial = 10
SaldoTodoDia = 5
taxa = 1.01

while i < mesesInvestidos:
    soma += taxa ** i
    i += 1

investimento = saldoInicial * taxa ** mesesInvestidos + SaldoTodoDia * soma
print(investimento)
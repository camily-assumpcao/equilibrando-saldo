"""
Para esse desafio, considere que você foi contratado por uma empresa bancária para auxiliar nas implementações e melhorias do sistema 
empresarial. Em uma análise inicial, foi identificado pela equipe financeira a necessidade de desenvolver uma solução que permita ao 
cliente equilibrar seu saldo bancário. Dessa forma, o programa deve solicitar uma entrada que representa o saldo atual do funcionário, 
e após, seja informado o valor de duas transações, sendo elas: um depósito e um saque. O programa deve atualizar o saldo com base nas 
transações e exibir o saldo final.
"""

# Número de iterações
num_transacoes = int(input("Quantas transações deseja processar? "))

for i in range(num_transacoes):
    print(f"\nTransação {i + 1}:")
    
    # Entrada de dados
    saldo_atual = float(input("Informe o saldo atual: "))
    valor_deposito = float(input("Informe o valor do depósito: "))
    valor_retirada = float(input("Informe o valor da retirada: "))

    # Processamento
    saldo_atualizado = saldo_atual + valor_deposito - valor_retirada

    # Saída
    print(f"Saldo atualizado na conta: {saldo_atualizado:.1f}")

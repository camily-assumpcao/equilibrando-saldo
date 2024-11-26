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

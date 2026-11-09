"""
Exercício 10 - Medio

Enunciado:
Simule um caixa eletrônico.

# Objetivo:
# Resolva este exercício sem consultar a resposta.
# Planeje, codifique, teste e refatore.
"""

# Escreva sua solução abaixo:
 
saque = 400 # float(input("Insira o dinheiro : "))

saldo = 500

saldo_atual = saldo-saque

print(f"Saldo R$ {saldo_atual}")

novo_saque = 0
if saldo_atual <0:
    print("Saldo insuficiente")
elif saldo_atual == 0:
    print("Saldo zerado , sem saque")
else:
    print("Saldo realizado com sucesso! ")
    print(f"Saldo R${saldo_atual}")








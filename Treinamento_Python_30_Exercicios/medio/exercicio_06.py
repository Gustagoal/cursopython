"""
Exercício 6 - Medio

Enunciado:
Leia um arquivo texto e conte linhas.

# Objetivo:
# Resolva este exercício sem consultar a resposta.
# Planeje, codifique, teste e refatore.
"""

# Escreva sua solução abaixo:


with open("teste.txt","r") as arquivo:
    # for c in range(10):
        # arquivo.write("Ola\r")
        print(len(arquivo.readlines()))

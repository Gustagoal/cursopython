"""
Exercício 1 - Medio

Enunciado:
Crie um jogo de adivinhação.

# Objetivo:
# Resolva este exercício sem consultar a resposta.
# Planeje, codifique, teste e refatore.
"""

# Escreva sua solução abaixo:

palavra = "cenoura"
palavra_adivinha = []

adivinhar = input("Chute uma letra : ")

for letra in palavra:
    palavra_adivinha+=letra

for c in range(1,11):
    if adivinhar in palavra_adivinha:
        print("Acertou a Letra")
    else:
        print("Errou a letra") 
        
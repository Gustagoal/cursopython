"""
Exercício 4 - Medio

Enunciado:
Conte frequência de palavras em um texto.

# Objetivo:
# Resolva este exercício sem consultar a resposta.
# Planeje, codifique, teste e refatore.
"""

# Escreva sua solução abaixo:

text = "Hello How are you"

text_separete = text.split()

contagem = 0

for word in text_separete:
    if word in text_separete:
        contagem+=1
print(f"A palavra {word} apareceu {contagem} vezes ")
"""
Exercício 4 - Medio

Enunciado:
Conte frequência de palavras em um texto.

# Objetivo:
# Resolva este exercício sem consultar a resposta.
# Planeje, codifique, teste e refatore.
"""

# Escreva sua solução abaixo:

text = "Bom dia , hoje o dia esta bonito"


for word in text.split():
    if word == word:
        contagem = word.count(word)
        print(f"A palavra {word} apareceu {word.count(word)} ")
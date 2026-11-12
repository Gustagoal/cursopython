"""
Exercício 7 - Medio

Enunciado:
Crie uma agenda usando dicionários.

# Objetivo:
# Resolva este exercício sem consultar a resposta.
# Planeje, codifique, teste e refatore.
"""

# Escreva sua solução abaixo:


manha = input("write your active in the morning :  ")
tarde = input("write your active in the afternoon :  ")
noite = input("write your active in the evening :  ")

tarefas = {"Morning":manha,
           "Afternoon":tarde ,
           "Evening":noite}


print(f" Minha rotina pela manhã é : {tarefas["Morning"]}")
print(f" Minha rotina pela tarde é : {tarefas["Afternoon"]}")
print(f" Minha rotina pela noite é : {tarefas["Evening"]}")




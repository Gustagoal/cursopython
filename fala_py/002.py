import pyttsx3 # Importação da biblioteca
import keyboard 
engine = pyttsx3.init() # Inicialização da biblioteca 

soco = engine.say("Você selecionou o comando socô ") # Passando a mensagem 
comando = input("Digite um ataque : ")

if comando == "q":
    print(soco)
    engine.runAndWait() # Colando o codigo para rodar 

# voices = engine.getProperty("voices")





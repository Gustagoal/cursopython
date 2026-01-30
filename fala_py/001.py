import pyttsx3 # Importação da biblioteca

engine = pyttsx3.init() # Inicialização da biblioteca 

engine.say("Ola , tudo bem ") # Passando a mensagem 

voices = engine.getProperty("voices")

print(voices)

engine.runAndWait() # Colando o codigo para rodar 



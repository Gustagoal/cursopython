from selenium import webdriver
from selenium.webdriver.common.by import By
import time
time.sleep(5)

navegador = webdriver.Chrome()
navegador.get("https://www.youtube.com/")

procurar = navegador.find_element(By.NAME,"search_query")
procurar.send_keys("Abertura de Dragon ball GT")
procurar = navegador.find_element(By.CLASS_NAME,"ytSearchboxComponentSearchButton").click



time.sleep(5)
input("Digite para encerrar")
navegador.quit()

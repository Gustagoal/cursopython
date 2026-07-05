from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument("--headless") 

driver = webdriver.Chrome(options=options)

driver.get("https://www.youtube.com/watch?v=qr3zfkvuMDM&list=RD1Z-8YUbRUZk&index=2")
sleep(2)

input("Pressione Enter para sair...")
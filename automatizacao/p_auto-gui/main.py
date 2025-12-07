import pyautogui

pyautogui.PAUSE = 4 # Coloca 1 segundo de pausa


pyautogui.press("win")
pyautogui.write("Google")

pyautogui.press("enter")
pyautogui.write("https://www.youtube.com/")
pyautogui.press("enter")

# pyautogui.position() mostra a posição do mouse

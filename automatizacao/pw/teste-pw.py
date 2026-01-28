from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    page = navegador.new_page()

    page.goto("https://www.youtube.com/")

    print(page.title()) 

navegador.close()
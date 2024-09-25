#navegador.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def iniciar_navegador():
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def esperar_carregamento(driver):
    try:
        # Substitua 'id_do_elemento' pelo ID de um elemento que indica que a página carregou
        elemento = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/cpit-app/fx-app-shell/div/div/header/mat-toolbar/div[1]/a/img'))
        )
    except:
        print('Tempo de espera excedido.')

import pyautogui
import pytesseract
import cv2
import numpy as np
from pyscreeze import ImageNotFoundException
import time

def localizar_texto_e_clicar(texto_procurado):
    screenshot = pyautogui.screenshot()
    imagem = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    dados = pytesseract.image_to_data(imagem, lang='por', output_type=pytesseract.Output.DICT)

    for i in range(len(dados['text'])):
        texto = dados['text'][i].strip()
        if texto_procurado.lower() in texto.lower():
            x = dados['left'][i] + dados['width'][i] // 2
            y = dados['top'][i] + dados['height'][i] // 2
            pyautogui.moveTo(x, y)
            pyautogui.click()
            return True
    return False

def clicar_imagem(imagem_referencia, max_attempts=30, interval=1, confidence=0.8):
    attempts = 0
    while attempts < max_attempts:
        try:
            posicao = pyautogui.locateCenterOnScreen(imagem_referencia, confidence=confidence)
            if posicao is not None:
                pyautogui.moveTo(posicao)
                pyautogui.click()
                return True
            else:
                print(f'Imagem "{imagem_referencia}" não encontrada. Tentando novamente ({attempts + 1}/{max_attempts})...')
                attempts += 1
                time.sleep(interval)
        except ImageNotFoundException:
            print(f'Imagem "{imagem_referencia}" não encontrada. Tentando novamente ({attempts + 1}/{max_attempts})...')
            attempts += 1
            time.sleep(interval)
    print(f'Imagem "{imagem_referencia}" não encontrada após {max_attempts} tentativas.')
    return False

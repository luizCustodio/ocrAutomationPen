#ocr.py
import pyautogui
import pytesseract
import cv2
import numpy as np

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

def clicar_imagem(imagem_referencia):
    posicao = pyautogui.locateCenterOnScreen(imagem_referencia, confidence=0.8)
    if posicao is not None:
        pyautogui.moveTo(posicao)
        pyautogui.click()
        return True
    else:
        print(f'Imagem "{imagem_referencia}" não encontrada.')
        return False

# Automação de Cliques com OCR e PyAutoGUI

## Descrição

Este projeto é um script Python que automatiza interações com a interface gráfica do usuário, como cliques em botões e seleção de itens, utilizando reconhecimento óptico de caracteres (OCR) e controle do mouse. O script percorre uma lista de itens, localiza cada um deles na tela através do texto exibido ou imagens de referência, e executa ações predefinidas, como clicar em botões específicos e salvar páginas como PDF.

## Pré-requisitos

- **Python 3.x**
- **Bibliotecas Python**:
  - [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
  - [pytesseract](https://pypi.org/project/pytesseract/) (biblioteca Python para interagir com o Tesseract OCR)
  - [OpenCV](https://pypi.org/project/opencv-python/)
  - [Selenium](https://pypi.org/project/selenium/)
- **Tesseract OCR**:
  - [Download do Tesseract OCR para Windows](https://github.com/UB-Mannheim/tesseract/wiki)
- **Dados de Treinamento em Português para o Tesseract**:
  - [Download do arquivo `por.traineddata`](https://github.com/tesseract-ocr/tessdata/blob/main/por.traineddata)
- **ChromeDriver**:
  - [Download do ChromeDriver](https://chromedriver.chromium.org/downloads)
- **Google Chrome**:
  - Necessário para controle do navegador via depuração remota
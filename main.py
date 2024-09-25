# main.py
import time
import pytesseract
import pyautogui
from utils.ocr import localizar_texto_e_clicar, clicar_imagem
from utils.navegador import iniciar_navegador, esperar_carregamento
from selenium.webdriver.common.by import By

# Configurar o caminho do Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Iniciar o navegador
driver = iniciar_navegador()

# Lista de nomes dos itens a serem clicados
lista_itens = [
    'ADIB',
    'ALCAR',
    'ALERT',
    'BONN',
    'ALUTRAT',
    'AMAZON',
    'ANIDRO',
    'ARCUS',
    'AREIA',
    'ATOLINI',
    'BANDEIRANTES',
    'BBS',
    'BEAPLAST',
    'BERLINERLUFT',
    'BIEHL METALURGICA',
    'BISCOITO JUVIS',
    'BLASS COMPONENTES',
    'BOI BAIO',
    'BOTTCHER',
    'BRASIL TEMPER',
    'BRITA FUCHS',
    'BRITA IBIRUBA',
    'BRITADOR TUPY',
    'BRITAGEM SOLEDADE RS',
    'BRITAXAN',
    'CABEL',
    'CALDLASE',
    'CAPRINI',
    'CASTER SUL',
    'CEOLIN E CIA',
    'CERAMICA OURITELHA',
    'CERB CONSTRUTORA',
    'CEREALISTA MARX',
    'CHAPEMEC',
    'COACRIS',
    'COAPIL',
    'COMERCIAL REIS',
    'COMIVA',
    'CONCREVALE',
    'CONCREXAP',
    'CONDOVILLE',
    'CONFINA',
    'CONSTRUTORA RIOMAX',
    'COOP PASTORIL',
    'COOPECA',
    'COOPECA RS',
    'CYCLEVIDRO',
    'DANGLASS',
    'DEALE',
    'DEGRAFICA',
    'DEZ ALIMENTOS',
    'DOMPEL',
    'DRYKO',
    'EKOPLASTIC',
    'EZY COLOR',
    'FAQUILAMINAS',
    'FCB INDUSTRIA',
    'FMG COM DE FERRO',
    'FMG FERROS LIGAS',
    'FORMPLAST',
    'FIGOIBI',
    'FRIOLACK',
    'FUNDICAO LUZITANA',
    'GESLA',
    'GIGLIO',
    'GIRASSOL ALIMENTOS',
    'GLOBORR',
    'GRAFFTEX',
    'GRUPO SOLAR',
    'HIPER FORTE',
    'HIPER FORTE INDUSTRIA',
    'HT MICRON',
    'HYVA',
    'ICO METAIS',
    'INDUSTRIA BRAIDO',
    'INDUSTRIAL KF',
    'IRRIGAPLAS',
    'ITABRAS',
    'ITAX',
    'ITAX CONSTRUTORA',
    'ITRON',
    'ITT BRASIL',
    'ITUMBIARA TEXTIL',
    'JANTSCH',
    'JARFLEX',
    'KELLY METAIS',
    'L&D MINERADORA',
    'LACTOVALE',
    'LATICIONIO LORENZO',
    'LATICINIO SANTIAGO',
    'LATICINIO BELOS MONTES',
    'LATICINIO GALVAO',
    'LATICINIO GRAN FILATA',
    'LECACAU CHOCOLATES',
    'LETAVO ALIMENTOS',
    'LIDERTEX',
    'LZK CONSTRUTORA',
    'MADEL',
    'MAR E RIO PESCADOS',
    'MASSATEMPER',
    'MERCOSUL  INDUSTRIA',
    'METALDYNE',
    'METALURGICA JAMA',
    'MIMAPLAS',
    'MINASSUL',
    'MINERADORA DE AGUAS GENEBRA',
    'MOVEIS CAFTOR',
    'MOVEIS CANCAO',
    'MOVEIS DACHERI',
    'MOVEIS SEMMER',
    'MP VALVULAS',
    'MULTINJET',
    'NACIONAL TUBOS',
    'NORTEVIDROS',
    'OLIMPLASTIC',
    'P GUARAPUAVA',
    'PEDREIRA TRIANGULO',
    'PEVE FOODS',
    'PICCININI',
    'PIETRO PEDRAZZA',
    'PLASUNIT',
    'PLEX VIDROS',
    'POLIDEC',
    'POTY AMBIENTAL',
    'PUMP AMERICA1 CL 514',
    'PUMP AMÉRICA',
    'PUMP AMÉRICA1',
    'QUALITY TECIDOS',
    'RAINHA ALIMENTOS',
    'RC ALIMENTOS',
    'REFRIGERANTES XUK',
    'REISAM',
    'RENNER MCFIL',
    'REVIPLAST',
    'RICCI',
    'ROSFRIOS',
    'ROSFRIOS ALIMENTOS',
    'SAO LEOPOLDO',
    'SEAN COUROS',
    'SEBO SOL',
    'SUPLAY',
    'TEM VIDROS',
    'TEMPERBRASILIA',
    'TEMPERFOZ',
    'TERMOPLASTCOS',
    'TEXTIL ITAJA',
    'TRATERM',
    'TRATERM LTDA',
    'TRATTEL',
    'TRITEC RS',
    'UNIMED RIO VERDE',
    'V W MADEIRAS',
    'VD FABRICA DE VIDROS',
    'VEGETALLIS',
    'VIDROBENS',
    'VITRINO',
    'ZETA PLASTICOS',
]

# Função para clicar em "Aplicar"
def clicar_aplicar():
    time.sleep(2)
    sucesso = clicar_imagem('assets/icones/aplicar.png')
    if not sucesso:
        print('Botão "Aplicar" não encontrado.')

# Função para clicar na engrenagem
def clicar_engrenagem():
    time.sleep(1)
    sucesso = clicar_imagem('assets/icones/engrenagem.png')
    if not sucesso:
        print('Engrenagem não encontrada.')

# Função para imprimir como PDF
def imprimir_como_pdf():
    sucesso = clicar_imagem('assets/icones/imprimir.png')
    if sucesso:
        time.sleep(1)
        # Selecionar "Página atual como PDF"
        sucesso_pdf = clicar_imagem('assets/icones/pdf.png')
        time.sleep(1)
        pyautogui.hotkey('ctrl', '1')
    else:
        print('Botão "Imprimir" não encontrado.')

# Variável global para contar os arquivos salvos
file_counter = 1

# Função para processar as abas extras
def processar_abas_extras():
    global file_counter  # Para modificar a variável global
    main_window = driver.current_window_handle
    # Obter todas as abas abertas, exceto a principal
    tabs_to_process = [handle for handle in driver.window_handles if handle != main_window]
    for tab_handle in tabs_to_process:
        # Mudar para a aba
        driver.switch_to.window(tab_handle)
        # Esperar até que a imagem 'impressora.png' seja encontrada
        max_wait_time = 300  # Tempo máximo de espera em segundos
        wait_time = 0
        sucesso_click1 = False
        while not sucesso_click1 and wait_time < max_wait_time:
            time.sleep(1)
            wait_time += 1
            sucesso_click1 = clicar_imagem('assets/icones/impressora.png')
            if not sucesso_click1:
                print(f"Tentativa {wait_time}: Imagem 'impressora.png' não encontrada na aba. Tentando novamente...")
        if not sucesso_click1:
            print("Tempo de espera excedido para encontrar a imagem 'impressora.png' na aba.")
            # Fechar a aba e continuar
            pyautogui.hotkey('ctrl', 'w')
            continue
        # Executar o segundo clique
        time.sleep(1)
        sucesso_click2 = clicar_imagem('assets/icones/imprimirb.png')
        if not sucesso_click2:
            print("Não foi possível realizar o segundo clique na imagem 'imprimirb.png'.")
        # Esperar a janela de salvar arquivo aparecer
        time.sleep(2)
        # Digitar o número único como nome do arquivo
        pyautogui.typewrite(str(file_counter))
        file_counter += 1
        # Clicar em "Salvar"
        sucesso_save = clicar_imagem('assets/icones/salvar.png')
        if not sucesso_save:
            print('Botão "Salvar" não encontrado.')
        # Fechar a aba atual
        pyautogui.hotkey('ctrl', 'w')
    # Voltar para a janela principal
    driver.switch_to.window(main_window)

if __name__ == '__main__':
    item_counter = 0  # Contador de itens processados
    total_items = len(lista_itens)
    current_index = 0

    while current_index < total_items:
        item = lista_itens[current_index]

        # Antes de procurar o item, clicar no local especificado
        x_elemento = 588  # Coordenada X (ajuste conforme necessário)
        y_elemento = 639  # Coordenada Y (ajuste conforme necessário)
        pyautogui.moveTo(x_elemento, y_elemento)
        pyautogui.click()
        time.sleep(0.5)

        # Inicializa as tentativas de scroll
        scroll_attempts = 0
        item_found = False

        # Rolar para o topo antes de começar a procurar cada item
        pyautogui.scroll(10000)
        time.sleep(0.5)

        while not item_found:
            sucesso = localizar_texto_e_clicar(item)
            if sucesso:
                item_found = True
                clicar_aplicar()
                esperar_carregamento(driver)
                clicar_engrenagem()
                imprimir_como_pdf()
                item_counter += 1
                current_index += 1  # Avança para o próximo item
                break  # Sai do loop de tentativa
            else:
                # Se não encontrar, rola um pouco e tenta novamente
                scroll_amount = -200  # Valor negativo para rolar para baixo
                pyautogui.scroll(scroll_amount)
                time.sleep(0.5)
                scroll_attempts += 1

        # Após processar o item, verificar se é hora de processar as abas extras
        if item_counter > 0 and item_counter % 10 == 0:
            # Aguarda um pouco para garantir que todas as abas tenham sido abertas
            time.sleep(5)
            processar_abas_extras()
            # Após processar as abas, continuar com os itens restantes

    print("Processamento concluído.")

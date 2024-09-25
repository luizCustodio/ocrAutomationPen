#main.py
import time
import pytesseract
import pyautogui
from utils.ocr import localizar_texto_e_clicar, clicar_imagem
from utils.navegador import iniciar_navegador, esperar_carregamento

#"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:/ChromeDebug"

# Configurar o caminho do Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Iniciar o navegador
driver = iniciar_navegador()

# Lista de nomes dos itens a serem clicados
lista_itens = [
    'ADIB',
    'ALCAR',
    'ALERT'
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
    


    
    # Adicionar itens
]

# Função para clicar em "Aplicar"
def clicar_aplicar():
    time.sleep(2)
    #sucesso = localizar_texto_e_clicar('Aplicar')
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
        '''if sucesso_pdf:
            time.sleep(2)
            # Confirmar a impressão (salvar PDF)
            pyautogui.hotkey('ctrl', 's')
            time.sleep(1)
            pyautogui.press('enter')
        else:
            print('Opção "Página atual como PDF" não encontrada.')'''
    else:
        print('Botão "Imprimir" não encontrado.')

if __name__ == '__main__':
    for item in lista_itens:
        sucesso = localizar_texto_e_clicar(item)
        if sucesso:
            clicar_aplicar()
            esperar_carregamento(driver)
            clicar_engrenagem()
            imprimir_como_pdf()
        else:
            print(f'Item "{item}" não encontrado.')

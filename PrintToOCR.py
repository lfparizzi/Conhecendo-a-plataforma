from PIL import Image # Abrir a imagem no script
import pytesseract # Módulo da tecnologia OCR
import pyautogui as pg # Screenshot
from pynput import keyboard # listener de teclas
import os # clear screen ( cls do windows, no linux seria clear)
import keyboard  #qqkeyboard
import time # tempo
import pyperclip # passar o resultado para seu ctrl+v

# O algoritmo seleciona coordenadas de onde está seu mouse ao apertar determinada tecla (Q por padrão) no canto superior esquerdo
# e novamente do canto inferior direito de onde deseja selecionar a caixa para tirar o print da tela no quadrilatero designado
# a partir disso ele envia o print para o módulo de leitura OCR e retorna os valores fidedignos da imagem
# nota-se alguns problemas com o caractere 'ó'


os.system('cls')
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@ Algoritmo de Leitura OCR @@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n\n")

#parâmetros para a seleção de área pelo teclado
key = 'q' # aqui digitei a tecla para o funcionamento do programa
stop = False
def onkeypress(event):
    global stop
    if event.name == key:
        stop = True

# --------->
keyboard.on_press(onkeypress)
# --------->


# Coordenadas canto superior esquerdo
def GetPositionA():
    while True:  # loop
            try:  # se usuário apertar outra tecla não dará erro
                print("Aperte '"+key+"' no canto superior esquerdo da área a ser lida")
                time.sleep(1)
                if stop:  # se 'q' for pressionado
                    GetPositionA.ax,GetPositionA.ay = pg.position()
                    print("Posição identificada com sucesso >",pg.position(),"\n")
                    break  # quebra o loop
            except:
                print("#######")
                break  # se usuário apertar qualquer outra coisa quebra o loop

# Coordenadas canto inferior esquerdo
def GetPositionB():
    while True:  # loop
            try:  # se usuário apertar outra tecla não dará erro
                print("Aperte '"+key+"' no canto inferior direito do local que deseja ler")
                time.sleep(0.5)
                if stop:  #se +key+ for pressionado
                    GetPositionB.bx,GetPositionB.by = pg.position()
                    print("Posição identificada com sucesso >",pg.position(),"\n")
                    break  # quebra o loop
            except:
                print("#######")
                break  # se usuário apertar qualquer outra coisa quebra o loop


GetPositionA()

stop = False # temos que resetar o valor da variável para não termos problema quando rodar o GetPositionB()

GetPositionB()

#cria imagem da região selecionada
im = pg.screenshot(imageFilename='AreaSC.jpg',region=(GetPositionA.ax,GetPositionA.ay, GetPositionB.bx-GetPositionA.ax, GetPositionB.by-GetPositionA.ay))

#Linha excluisva para resolver problema de PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Parizzi\AppData\Local\Tesseract-OCR\tesseract.exe' 

#Extraindo o texto da imagem com a tecnologia OCR
OCR = pytesseract.image_to_string( Image.open('AreaSC.jpg') )
print(OCR)
pyperclip.copy(OCR) # passando o texto para seu CTRL+C
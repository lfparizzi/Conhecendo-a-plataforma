from PIL import Image # Abrir a imagem no script
import pytesseract # Módulo da tecnologia OCR
import pyautogui as pg # Screenshot

#achar um modo de automatizar esse processo com algum listener >> não consigo guardar as coordenadas no pg.position em variáveis
#podemos colocar um listener para um "selecionar área"
#podemos filtrar digitos das strings
input("Fique com o mouse no ponto superior esquerdo e aperte enter")
print(pg.position())
ax = int(input("Entre com o valor de X"))
ay = int(input("Entre com o valor de Y"))
input("Fique com o mouse no ponto inferior esquerdo e aperte enter")
print(pg.position())
bx = int(input("Entre com o valor de X"))
by = int(input("Entre com o valor de Y"))

#cria imagem na região selecionada
im = pg.screenshot(imageFilename='Teste.jpg',region=(ax,ay, bx-ax, by-ay))


pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Parizzi\AppData\Local\Tesseract-OCR\tesseract.exe' #resolvendo problema de Path

print( pytesseract.image_to_string( Image.open('Teste.jpg') ) ) # Extraindo o texto da imagem com tecnologia OCR
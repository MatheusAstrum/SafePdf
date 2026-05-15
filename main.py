import subprocess as s
import os
from PIL import Image
import time
import pyautogui

path = "saida/"
paginas = 0


def esquema_do_pdf(Pags):
    images = []
    for i in range(Pags):
        print(f"Abrindo local de saída => {path}")
        imagem = Image.open(f'saida/a{i}.png')
        print("Convertendo imagem para RGB.")
        imagem.convert('RGB')
        print("Adicionando imagem na lista.")
        images.append(imagem)
    if images:
        print("Salvando imagens como 'output.pdf'.")
        images[0].save(
            "output.pdf",
            "PDF",
            save_all=True,
            append_images=images[1:]
        )

def screen_shoot(Pags):
    try:
        paginas = Pags
        time.sleep(10)
        print("Começando em 10 segundos..")
        for numero in range(Pags):
            pyautogui.press("rightctrl")
            resposta = s.run(["scrot", "a.png"])
            pyautogui.click()
            pyautogui.press("right")
            os.system(f"mv a.png a{numero}.png")
            print(f"Arquivo -> 'a{numero}' renomeado.")
            os.system(f"mv a{numero}.png {path}")
            print(f"Arquivo -> 'a{numero}' movido para {path}.")
            print(f"Log scrot{resposta}")
            
        esquema_do_pdf(paginas)
        os.system(f"rm -rf {path}")
        print(f"Diretório -> {path} removido.")
    except Exception as e:
        print(f"error{e}")

def verifica_pasta():
    try:
        existe = os.path.exists(path)
        print(f"Verificando diretório padrão -> {path}")   
        
        if existe:

           # print("quantas paginas possue o pdf?")
           # print("Executando programa")
            num_pags = int(input("Número de páginas: "))
            print(num_pags)
            screen_shoot(num_pags)

        else:
            print(f"Criando diretório -> {path}")
            os.system(f"mkdir {path}")
            print("Qual o número total de páginas no pdf?")
            num_pags = int(input("numero de paginas: "))
            print(num_pags)
            screen_shoot(num_pags)

    except Exception as e:
        print(f"error:{e}")

def main():
    verifica_pasta()
main()

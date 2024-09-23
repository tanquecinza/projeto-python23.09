"""""
import tkinter as tk
from tkinter import font
tela = tk.Tk()
tela.title("minha primeira janela")
tela.geometry("500x400")

fonte1 = font.Font(family="algerian", size=22)
fonte2 = font.Font(family="algerian", size=22)

label = tk.Label(tela, text ="nome", font=fonte1)
label.pack(pady=10)
caixa_texto = tk.Entry(tela)
caixa_texto.pack(pady=5)

label = tk.Label(tela, text ="sobrenome",font=fonte2)
label.pack(pady=5)
caixa2 = tk.Entry(tela)
caixa2.pack(pady=5)

def nome_sobrenome_click():
    nome = caixa_texto.get()
    sobrenome = caixa2.get()
    label_nome_sobrenome.config(text="seu nome é :" + nome + " " + sobrenome)

botao = tk.Button(tela, text="botao", command= nome_sobrenome_click)
botao.pack(pady=5)

label_nome_sobrenome = tk.Label(tela,text="")
label_nome_sobrenome.pack(pady=4)

caixa_selecao = tk.Checkbutton(tela,text="check")
caixa_selecao.pack(pady=2)

caixa_opcao = tk.Radiobutton(tela,text="ligado")
caixa_opcao.pack(pady=2)

caixa_multilinha = tk.Text(tela,height=2,width=30)
caixa_multilinha.pack(pady=2)
"""""

"""""
import tkinter as tk

tela = tk.Tk()
canvas = tk.Canvas(tela, width=500,height=200)
canvas.pack(tela.mainloop()pady=10)
canvas.create_arc(0,0,500,200)


"""""
"""""
import tkinter as tk

tela = tk.Tk()
tela.geometry("500x400")
listbox = tk.Listbox(tela,width=500,height=200)
listbox.pack()
listbox.insert(tk.END, "honda")
listbox.insert(tk.END, "toyta")
listbox.insert(tk.END, "nissan")
listbox.insert(tk.END, "volks")

tela.mainloop()
"""""
"""""
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from cProfile import label
from tkinter import font
def config():
    print("salvo")

tela = tk.Tk()
tela.title("menu personalizado")
tela.geometry("500x400")
config_personalizada = tk.Menu(tela)
tela.config(menu=config_personalizada)

file_menu = tk.Menu(config_personalizada, tearoff= 0)
config_personalizada.add_cascade(label="menu", menu=file_menu)
file_menu.add_command(label="copy", command=config)
file_menu.add_command(label="cut", command=config)
file_menu.add_command(label="open", command=config)
file_menu.add_command(label="salvar", command=config)

tela.mainloop()
"""""

import tkinter as tk
from PIL import Image
import requests
from io import BytesIO
from cProfile import label
from tkinter import font

def page_imagem(link_da_imagem):
    resposta_do_site = requests.get(link_da_imagem)
    imagem_site = BytesIO(resposta_do_site.content)
    imagem = Image.open(imagem_site)
    imagem = imagem.convert("RGB")
    return imagem

def converter(imagem):
    with BytesIO() as output:
        imagem.save(output, format= "PPM")
        ppm_imagem = output.getvalue()
    return ppm_imagem


imagem_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvGFZ0DHhLEoQPdHbpFVRb5vWnxaelPqspGxoBNsGH3yZihOVB36tWDdbh2Gt-GyXoiS8&usqp=CAU"


tela = tk.Tk()
tela.title("menu personalizado")
tela.geometry("1200x900")
config_personalizada = tk.Menu(tela)
tela.config(menu=config_personalizada)

canva = tk.Canvas(tela, width=1000,height=1000)
canva.pack(pady=10)

imagem = page_imagem(imagem_url)
imagem_ppm = converter(imagem)
imagem = tk.PhotoImage(data=imagem_ppm)
image_canva = canva.create_image(300, 300, image=imagem)

import tkinter as tk

def config():
    print("salvo")

tela.title("menu personalizado")
tela.geometry("500x400")
config_personalizada = tk.Menu(tela)
tela.config(menu=config_personalizada)

def abrir_imagem1(url_imagem):
    nova_imagem = page_imagem(url_imagem)
    nova_imagem_ppm = converter(nova_imagem)
    nova_imagem = tk.PhotoImage(data=nova_imagem_ppm)

    canva.itemconfig(image_canva,image= nova_imagem)
    canva.image = nova_imagem

def ferrari():
    url_imagem = "https://img.freepik.com/psd-gratuitas/carro-branco-isolado_176382-1486.jpg"
    abrir_imagem1(url_imagem)

def mclaren():
    url_imagem = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-Ym8_82fOtrokmsoG82UI0ZOpcf_4p3oCRdsN2HA-Nlw5pIIY_yhTSOd6g38qyIdRR0Q&usqp=CAU"
    abrir_imagem1(url_imagem)

def franchesco_virguline():
    url_imagem = "https://p15-kimg.kwai.net/kimg/EKzM1y8qmgEKAnMzEg1waG90by1vdmVyc2VhGoQBdXBpYy8yMDIxLzEwLzIwLzExL0JNakF5TVRFd01qQXhNVEF3TXpCZk1UVXdNREF4TURVME5USXhNVGMyWHpFMU1EQTJNREkyT0RrME5EUXdOVjh5WHpNPV9vZmZuX0JlOTZmNjYyNGY3OThiMTY5YzMyNWFiZTUyZTNiYzE2NC53ZWJw.webp"
    abrir_imagem1(url_imagem)

file_menu = tk.Menu(config_personalizada, tearoff= 0)
config_personalizada.add_cascade(label="carteira de carros", menu=file_menu)
file_menu.add_command(label="imagem1", command=ferrari)
file_menu.add_command(label="imagem2", command=mclaren)
file_menu.add_command(label="imagem3", command=franchesco_virguline)


tela.mainloop()
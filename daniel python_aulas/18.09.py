"""""
import tkinter as tk
from tkinter import font
tela = tk.Tk()
tela.title("minha primeira janela")
tela.geometry("500x400")

def on_click(event):
    print("click detectado:", event.x, event.y)

def on_motion(event):
    print("movimento detectado:", event.x, event.y)

tela.bind("<Button-1>", on_click)
tela.bind("<Motion>", on_motion)

tela.mainloop()
"""""
"""""
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from cProfile import label
from tkinter import font

tela = tk.Tk()
tela.title("janela")
tela.geometry("500x400")

fonte1 = font.Font(family="arial", size=22)
label = tk.Label(tela, text ="Sua coordenada é:", font=fonte1)
label.pack(pady=10)


def on_keypress(event):
    print("tecla pressionada:", event.char)

def on_click(event):
    print("click detectado:", event.x, event.y)
    label_click.config(text="coordenada do click:"+ str(event.x)+"  " + str(event.y))

tela.bind("<KeyPress>", on_keypress)
tela.bind("<Button-1>", on_click)

label_click = tk.Label(tela, text="")
label_click.pack(pady=4)

tela.mainloop()
"""""

import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from cProfile import label
from tkinter import font

def pegar_pokemon(pokemon):
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
    qual_pokemon = requests.get(url)
    qual_pokemon = qual_pokemon.json()
    imagem = qual_pokemon['sprites']['front_default']
    return imagem

def pegar_pokemon2():
    url = "https://pokeapi.co/api/v2/pokemon?limit=1000"
    qual_pokemon1 = requests.get(url)

def page_imagem(link_da_imagem):
    resposta_do_site = requests.get(link_da_imagem)
    imagem_site = BytesIO(resposta_do_site.content)
    imagem = Image.open(imagem_site)
    imagem = imagem.convert("RGB")
    return imagem

def abrir_imagem1(url_imagem):
    nova_imagem = page_imagem(url_imagem)
    nova_imagem_ppm = converter(nova_imagem)
    nova_imagem = tk.PhotoImage(data=nova_imagem_ppm)
    canva.itemconfig(image_canva, image=nova_imagem)
    canva.image = nova_imagem


def converter(imagem):
    with BytesIO() as output:
        imagem.save(output, format= "PPM")
        ppm_imagem = output.getvalue()
    return ppm_imagem

def pokemon():
    pokemon_digitado = caixa2.get()
    url_imagem = pegar_pokemon(pokemon_digitado)
    abrir_imagem1(url_imagem)

tela = tk.Tk()
tela.title("janela")
tela.geometry("500x400")


canva = tk.Canvas(tela, width=350,height=300)
canva.pack(pady=10)


image_canva = canva.create_image(100, 100)

caixa2 = tk.Entry(tela)
caixa2.pack(pady=5)

botao = tk.Button(tela, text="botao", command=pokemon)
botao.pack(pady=5)


tela.mainloop()
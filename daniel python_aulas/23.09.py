import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from cProfile import label
from tkinter import font
from tkinter import ttk

def pegar_pokemon(pokemon):
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
    qual_pokemon = requests.get(url)
    qual_pokemon = qual_pokemon.json()
    imagem = qual_pokemon['sprites']['front_default']
    return imagem


def pegar_pokemon2():
    url = "https://pokeapi.co/api/v2/pokemon?limit=1302"
    qual_pokemon1 = requests.get(url)
    qual_pokemon1 = qual_pokemon1.json()
    pokemons = qual_pokemon1['results']
    pokedex = []
    for pokemon in pokemons:
        pokedex.append(pokemon['name'])
    return pokedex


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
        imagem.save(output, format="PPM")
        ppm_imagem = output.getvalue()
    return ppm_imagem


def pokemon():
    pokemon_digitado = caixa2.get()
    url_imagem = pegar_pokemon(pokemon_digitado)
    abrir_imagem1(url_imagem)

def poke_combobox(event):
    pokemon_digitado = pc.get()
    url = pegar_pokemon(pokemon_digitado)
    abrir_imagem1(url)

tela = tk.Tk()
tela.title("janela")
tela.geometry("500x400")

canva = tk.Canvas(tela, width=350, height=300)
canva.pack(pady=10)

image_canva = canva.create_image(100, 100)

caixa2 = tk.Entry(tela)
caixa2.pack(pady=5)

pokedex = pegar_pokemon2()
pc = ttk.Combobox(tela, values=pokedex)
pc.bind("<<ComboboxSelected>>",poke_combobox)
pc.pack(pady=5)


botao = tk.Button(tela, text="botao", command=pokemon)
botao.pack(pady=5)

tela.mainloop()
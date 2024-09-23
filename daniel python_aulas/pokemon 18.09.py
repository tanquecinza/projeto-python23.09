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

print pegar_pokemon(""))

tela = tk.Tk()
tela.title("janela")
tela.geometry("500x400")

fonte1 = font.Font(family="arial", size=22)
label = tk.Label(tela, text ="Sua coordenada é:", font=fonte1)
label.pack(pady=10)

tela.mainloop()
"""""

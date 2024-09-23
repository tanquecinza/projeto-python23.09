"""""
class biblioteca:
    def __init__(self, livro, estante, caixa):
        self.livro = livro
        self.estante = estante
        self.caixa = caixa
    def pegar_livro_emprestado(self):
        print ("foi pega o", self.livro)
    def pegar_livro_na_estante (self):
        print ("peguei o", self.livro, "na estante" , self.estante)
    def pagar_livro_no_caixa_livre (self):
        print ("paguei o livro",self.livro, "no", self.caixa)
biblioteca1 = biblioteca("peppa pig", 23, "caixa")
biblioteca1.pegar_livro_emprestado()
biblioteca1.pegar_livro_na_estante()
biblioteca1.pagar_livro_no_caixa_livre()
"""""
"""""
class pessoa:
    def __init__(self, rg, cpf, comprovante_residencia, nome, idade):
        self.rg = rg
        self.cpf = cpf
        self.comprovante_residencia = comprovante_residencia
        self.nome = nome
        self.idade = idade
    def estudante(self):
        print(self.nome, "esta estudando")

class aluno(pessoa):
    def __init__(self,rg, cpf, comprovante_residencia, nome,nota, idade, fome):
        super().__init__(rg, cpf, comprovante_residencia, nome, idade,)
        self.nota = nota
        self.fome = fome
    def fazer_prova(self):
        print("o aluno", self.nome, "esta fazendo prova")


aluno1 = aluno(54789,13141,"foto","daniel",10, 17,"muita fome")
aluno1.fazer_prova()

"""""
"""""
class pessoa:
    def __init__(self, rg, cpf, comprovante_residencia, nome, idade):
        self.rg = rg
        self.cpf = cpf
        self.comprovante_residencia = comprovante_residencia
        self.nome = nome
        self.idade = idade
    def professor(self):
        print(self.nome, "esta corrigindo")

class professor(pessoa):
    def __init__(self,rg, cpf, comprovante_residencia, nome,nota, idade, explica, corrige):
        super().__init__(rg, cpf, comprovante_residencia, nome, idade,)
        self.nota = nota
        self.explica = explica
        self.corrige = corrige
    def corrigir_prova(self):
        print("o professor", self.nome, "esta corrigindo prova do aluno daniel")

professor1 = professor(234,4334,"foto","albert", -0, 10,"explica bem", "para corrigir muito chato")
professor1.corrigir_prova()
"""""
"""""
class conta:
    def __init__(self, titular,saldo):
        self.titular = titular
        self.saldo = saldo

    def mostar_saldo(self):
        print("saldo de", self.titular, "é", self.saldo)
    def depositar (self, valor):
        if valor > 0:
            self.saldo = self.saldo + valor
            print("deposito realizado")
        else:
            print("valor invalido")

    def saque(self, valor):
        if valor < 0:
            print("valor invalido")
        elif valor <= self.saldo:
            self.saldo = self.saldo - valor
            print("saque realizado")
        else:
            print("valor invalido")

conta = conta("daniel",12.00)
conta.mostar_saldo()
conta.depositar(2000)
"""""
"""""
import tkinter as tk
from tkinter import font
tela = tk.Tk()
tela.title("minha primeira janela")
tela.geometry("350x400")

fonte1 = font.Font(family="algerian", size=24)
fonte2 = font.Font(family="calibri light", size=22)
fonte3 = font.Font(family="algerian", size=10)

label = tk.Label(tela, text ="bloco de notas", font=fonte1)
label.pack(pady=20)
label = tk.Label(tela, text ="truco",font=fonte2)
label.pack(pady=20)
label =tk.Label(tela, text="gool",font=fonte3)
label.pack(pady=20)

botao = tk.Button(tela, text="botao")
botao.pack(pady=60)

caixa_texto = tk.Entry(tela)
caixa_texto.pack(pady=5)

tela.mainloop()

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

tela.mainloop()